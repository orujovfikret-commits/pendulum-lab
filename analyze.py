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
implied_length = 9.81 * (period / (2 * np.pi)) ** 2

print(f"Sampling Frequency (fs): {fs:.2f} Hz")
print(f"Dominant Frequency: {dominant_freq:.3f} Hz")
print(f"Measured Period (T): {period:.3f} s")
print(f"Implied Length (L): {implied_length:.3f} m ({implied_length*100:.1f} cm)")
