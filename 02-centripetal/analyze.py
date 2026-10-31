import glob
import os
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

all_files = sorted(glob.glob("data/R*.csv"))
files = [f for f in all_files if "only" not in f]

results = []
os.makedirs("plots", exist_ok=True)

for f in files:
    name = os.path.basename(f)
    R = float(name.split("_")[0].replace("R", ""))

    df = pd.read_csv(f)
    t = df["Time (s)"].values if "Time (s)" in df.columns else df.iloc[:, 0].values

    gyro_cols = [c for c in df.columns if "Gyroscope" in c]
    gyro_col = next((c for c in gyro_cols if "z" in c.lower()), gyro_cols[0] if gyro_cols else df.columns[1])

    accel_cols = [c for c in df.columns if "Acceleration" in c or "accel" in c.lower()]
    accel_col = next((c for c in accel_cols if "z" in c.lower()), accel_cols[0] if accel_cols else df.columns[2])

    omega = df[gyro_col].values
    accel = df[accel_col].values

    mask = (omega > 0.5) & (t < t[-1] - 1.0)
    t_clean = t[mask]
    omega_clean = omega[mask]
    accel_clean = accel[mask]

    omega_sq = omega_clean ** 2

    (R_fit, c), cov = np.polyfit(omega_sq, accel_clean, 1, cov=True)
    R_fit_err = np.sqrt(cov[0, 0])

    results.append({
        "file": name,
        "R_measured": R,
        "R_fit": R_fit,
        "R_fit_err": R_fit_err,
        "c": c
    })

    print(f"File: {name} | R_measured: {R} | R_fit: {R_fit:.4f} +/- {R_fit_err:.4f} | c: {c:.4f}")

    plt.figure(figsize=(8, 4))
    plt.plot(omega_sq, accel_clean, label="Data")
    plt.plot(omega_sq, R_fit * omega_sq + c, "r-", label=f"Fit: a = {R_fit:.3f}*omega^2 + {c:.3f}")
    plt.xlabel("omega^2 (rad^2/s^2)")
    plt.ylabel("Acceleration (m/s^2)")
    plt.title(f"{name} Acceleration vs Omega^2")
    plt.legend()
    plt.grid(True)
    plt.savefig(f"plots/{name.replace('.csv', '')}_fit.png")
    plt.close()

data = pd.DataFrame(results)
R_meas = data["R_measured"].values
R_fit_vals = data["R_fit"].values

(k, d), cov_k = np.polyfit(R_meas, R_fit_vals, 1, cov=True)
k_err = np.sqrt(cov_k[0, 0])
d_err = np.sqrt(cov_k[1, 1])

print(f"\nSlope (k): {k:.4f} +/- {k_err:.4f}")
print(f"Intercept (d): {d:.4f} +/- {d_err:.4f}")

plt.figure(figsize=(8, 5))
plt.plot(R_meas, R_fit_vals, "ro", label="Data points")
plt.plot(R_meas, k * R_meas + d, "b-", label=f"R_fit = {k:.2f}*R + {d:.3f}")
plt.xlabel("Measured R (m)")
plt.ylabel("Fitted R_fit (m)")
plt.title("R_fit vs Measured R")
plt.legend()
plt.grid(True)
plt.savefig("plots/R_fit_vs_R.png")
plt.show()
