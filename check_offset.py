import glob
import os
import numpy as np
import pandas as pd
from scipy.signal import find_peaks

files = sorted(glob.glob("L*.csv"))
results = []

for f in files:
    name = os.path.basename(f)
    L_nominal = float(name.split("_")[0].replace("L", ""))

    df = pd.read_csv(f)
    t = df["Time (s)"].values
    dt = t[1] - t[0]

    mask = (t > 1.0) & (t < (t.max() - 1.0))
    df_clean = df[mask] if mask.sum() > 10 else df
    t_clean = df_clean["Time (s)"].values

    col = "Gyroscope y (rad/s)"
    if col not in df_clean.columns:
        col = df_clean.columns[1]

    s = df_clean[col].values

    peaks, _ = find_peaks(s, distance=int(0.4/dt), prominence=0.1)

    if len(peaks) > 1:
        periods = np.diff(t_clean[peaks])
        T = np.mean(periods)
    else:
        T = 0.0

    if T > 0:
        g_true = 9.81
        L_calculated = (g_true * (T**2)) / (4 * np.pi**2)
        offset_cm = (L_calculated - L_nominal) * 100

        results.append({
            "File": name,
            "L_nominal (m)": L_nominal,
            "T (s)": round(T, 3),
            "L_calc (m)": round(L_calculated, 3),
            "Offset (cm)": round(offset_cm, 1)
        })

df_res = pd.DataFrame(results).sort_values("L_nominal (m)")
print(df_res.to_string(index=False))
