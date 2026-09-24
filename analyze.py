import glob
import os
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
from scipy.signal import find_peaks

files = glob.glob("L*.csv")
results = []

for f in files:
    name = os.path.basename(f)
    L = float(name.split("_")[0].replace("L", ""))

    df = pd.read_csv(f)
    t = df["Time (s)"].values
    dt = np.mean(np.diff(t))

    mask = (t > 1.0) & (t < (t.max() - 1.0))
    df_clean = df[mask] if mask.sum() > 10 else df

    col = "Gyroscope y (rad/s)"
    if col not in df_clean.columns:
        col = df_clean.columns[1]

    s = df_clean[col].values
    t_clean = df_clean["Time (s)"].values

    min_dist = int(0.6 / dt)
    peaks, _ = find_peaks(s, distance=min_dist, prominence=0.5)

    if len(peaks) > 1:
        peak_times = t_clean[peaks]
        periods = np.diff(peak_times)
        T = np.mean(periods)
    else:
        freqs = np.fft.rfftfreq(len(s), d=dt)
        fft_vals = np.abs(np.fft.rfft(s - np.mean(s)))
        valid = (freqs > 0.3) & (freqs < 2.0)
        T = 1.0 / freqs[valid][np.argmax(fft_vals[valid])]

    results.append({"L": L, "T": T, "T2": T**2, "file": name})

data = pd.DataFrame(results).sort_values("L")
L_vals = data["L"].values
T2_vals = data["T2"].values

m, c = np.polyfit(L_vals, T2_vals, 1)
g = (4 * np.pi**2) / m

n = len(L_vals)
residuals = T2_vals - (m * L_vals + c)
s_err = np.sqrt(np.sum(residuals**2) / (n - 2))
m_err = s_err / np.sqrt(np.sum((L_vals - np.mean(L_vals))**2))
g_err = (4 * np.pi**2 / (m**2)) * m_err

print(f"Slope (m): {m:.4f} +/- {m_err:.4f}")
print(f"Intercept (c): {c:.4f}")
print(f"g = {g:.2f} +/- {g_err:.2f} m/s^2")

plt.figure(figsize=(8, 5))
plt.plot(L_vals, T2_vals, "ro", label="Data points")
plt.plot(L_vals, m * L_vals + c, "b-", label=f"Fit: T^2 = {m:.2f}L + {c:.2f}")
plt.xlabel("Length L (m)")
plt.ylabel("T^2 (s^2)")
plt.title(f"Gravity Fit: g = {g:.2f} +/- {g_err:.2f} m/s^2")
plt.legend()
plt.grid(True)
plt.savefig("gravity_fit_plot.png")
plt.show()
