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

df_res = 1.0 / (time[-1] - time[0])
f_min = dominant_freq - df_res
f_max = dominant_freq + df_res

g_ref = 9.81
L_est = g_ref * (period / (2 * np.pi)) ** 2
L_min = g_ref * ((1/f_max) / (2 * np.pi)) ** 2
L_max = g_ref * ((1/f_min) / (2 * np.pi)) ** 2
L_err = (L_max - L_min) / 2

print(f"Sampling Frequency (fs): {fs:.2f} Hz")
print(f"Dominant Frequency: {dominant_freq:.3f} +/- {df_res:.3f} Hz")
print(f"Measured Period (T): {period:.3f} s")
print(f"Implied Length (using g=9.81 for validation): {L_est:.3f} +/- {L_err:.3f} m ({L_est*100:.1f} +/- {L_err*100:.1f} cm)")
