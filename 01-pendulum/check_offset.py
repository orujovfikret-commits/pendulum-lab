import glob
import os
import numpy as np
import pandas as pd
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
g_standard = 9.81

print(f"{'File':<18} | {'L_nominal (m)':<13} | {'T (s)':<6} | {'L_calc (m)':<10} | {'Offset (cm)':<10}")
print("-" * 65)

for f in files:
    name = os.path.basename(f)
    L_nom = float(name.split("_")[0].replace("L", ""))

    df = pd.read_csv(f)
    t = df["Time (s)"].values
    dt = t[1] - t[0]

    if "L0.50" in name:
        t_max_limit = 10.2
    elif "L0.70" in name:
        t_max_limit = 17.5
    else:
        t_max_limit = t.max() - 2.0

    mask = (t > 2.0) & (t < t_max_limit)
    df_clean = df[mask]
    t_clean = df_clean["Time (s)"].values

    col = AXIS.get(name, "Gyroscope y (rad/s)")
    if col not in df_clean.columns:
        col = df_clean.columns[1]

    s = df_clean[col].values
    peaks, _ = find_peaks(s, distance=int(0.8 / dt), prominence=0.1)

    if len(peaks) > 1:
        T = np.mean(np.diff(t_clean[peaks]))
    else:
        T = 0.0

    if T > 0:
        L_calc = (T**2 * g_standard) / (4 * np.pi**2)
        offset_cm = (L_calc - L_nom) * 100
        print(f"{name:<18} | {L_nom:<13.2f} | {T:<6.3f} | {L_calc:<10.3f} | {offset_cm:+10.1f}")