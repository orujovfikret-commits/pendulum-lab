import glob
import os
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
from scipy.signal import find_peaks

AXIS = {
    "L0.20_run1.csv": "Gyroscope y (rad/s)",
    "L0.20_run2.csv": "Gyroscope y (rad/s)",
    "L0.30_run1.csv": "Gyroscope y (rad/s)",
    "L0.30_run2.csv": "Gyroscope y (rad/s)",
    "L0.40_run1.csv": "Gyroscope y (rad/s)",
    "L0.40_run2.csv": "Gyroscope x (rad/s)",
    "L0.50_run1.csv": "Gyroscope y (rad/s)",
    "L0.50_run2.csv": "Gyroscope x (rad/s)",
    "L0.70_run1.csv": "Gyroscope y (rad/s)",
    "L0.70_run2.csv": "Gyroscope y (rad/s)"
}

files = sorted(glob.glob("L*.csv"))
results = []

for f in files:
    name = os.path.basename(f)
    L = float(name.split("_")[0].replace("L", ""))

    df = pd.read_csv(f)
    t = df["Time (s)"].values
    dt = t[1] - t[0]

    mask = (t > 1.0) & (t < (t.max() - 1.0))
    df_clean = df[mask]
    t_clean = df_clean["Time (s)"].values

    col = AXIS.get(name, "Gyroscope y (rad/s)")
    if col not in df_clean.columns:
        col = df_clean.columns[1]

    s = df_clean[col].values

    peaks, _ = find_peaks(s, distance=int(0.8 / dt), prominence=0.1)

    if len(peaks) > 1:
        periods = np.diff(t_clean[peaks])
        T = np.mean(periods)
    else:
        T = 0.0

    print(f"File: {name} | Axis: {col.split(' ')[1]} | T = {T:.3f} s")

    if T > 0:
        results.append({"L": L, "T": T, "T2": T ** 2})

data = pd.DataFrame(results).sort_values("L")
L_vals = data["L"].values
T2_vals = data["T2"].values

(m, c), cov = np.polyfit(L_vals, T2_vals, 1, cov=True)
m_err = np.sqrt(cov[0, 0])

g = (4 * np.pi ** 2) / m
g_err = g * (m_err / m)

print(f"\nSlope: {m:.3f} +/- {m_err:.3f}")
print(f"g = {g:.2f} +/- {g_err:.2f} m/s^2")

plt.figure(figsize=(8, 5))
plt.plot(L_vals, T2_vals, "ro", label="Data points")
plt.plot(L_vals, m * L_vals + c, "b-", label=f"T^2 = {m:.2f}L + {c:.2f}")
plt.xlabel("Length L (m)")
plt.ylabel("T^2 (s^2)")
plt.title(f"g = {g:.2f} m/s^2")
plt.legend()
plt.grid(True)
plt.savefig("gravity_fit_plot.png")
plt.show()
