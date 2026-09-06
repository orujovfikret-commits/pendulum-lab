import numpy as np
import pandas as pd

df = pd.read_csv('L0.21_run1.csv')

time = df['Time (s)'].values
signal = df['Gyroscope z (rad/s)'].values

dt = np.mean(np.diff(time))
fs = 1.0 / dt
n = len(signal)

frequencies = np.fft.rfftfreq(n, d=dt)
fft_spectrum = np.abs(np.fft.rfft(signal - np.mean(signal)))

dominant_freq = frequencies[1:][np.argmax(fft_spectrum[1:])]
period = 1.0 / dominant_freq

# Spectral resolution error bound
df_res = 1.0 / (time[-1] - time[0])

# Single-point gravitational acceleration calculation (L = 0.21 m)
L = 0.21
L_err = 0.01
g_calc = (4 * np.pi**2 * L) / (period**2)

# Uncertainty propagation: dg/g = dL/L + 2*dT/T
T_err = df_res / (dominant_freq**2)
g_err = g_calc * ((L_err / L) + (2 * T_err / period))

print(f"Sampling Frequency (fs): {fs:.2f} Hz")
print(f"Dominant Frequency: {dominant_freq:.3f} +/- {df_res:.3f} Hz")
print(f"Measured Period (T): {period:.3f} +/- {T_err:.3f} s")
print(f"Calculated g: {g_calc:.2f} +/- {g_err:.2f} m/s^2")
