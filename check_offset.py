import glob
import os
import numpy as np
import pandas as pd

files = glob.glob("L*.csv")
results = []

for f in files:
    name = os.path.basename(f)
    L_nominal = float(name.split("_")[0].replace("L", ""))

    df = pd.read_csv(f)
    t = df["Time (s)"].values
    dt = np.mean(np.diff(t))

    col = "Gyroscope y (rad/s)"
    if col not in df.columns:
        col = df.columns[1]

    mask = (t > 1.0) & (t < (t.max() - 1.0))
    df_clean = df[mask] if mask.sum() > 10 else df

    s = df_clean[col].values
    freqs = np.fft.rfftfreq(len(s), d=dt)
    fft_vals = np.abs(np.fft.rfft(s - np.mean(s)))

    valid = (freqs > 0.3) & (freqs < 2.5)
    sub_freqs = freqs[valid]
    sub_fft = fft_vals[valid]
    freq = sub_freqs[np.argmax(sub_fft)]

    T = 1.0 / freq
    g_true = 9.81
    L_calculated = (g_true * (T**2)) / (4 * np.pi**2)
    offset_cm = (L_calculated - L_nominal) * 100

    results.append({
        "File": name,
        "L_nominal (m)": L_nominal,
        "T (s)": round(T, 4),
        "L_calc (m)": round(L_calculated, 4),
        "Offset (cm)": round(offset_cm, 2)
    })

df_res = pd.DataFrame(results).sort_values("L_nominal (m)")
print(df_res.to_string(index=False))
