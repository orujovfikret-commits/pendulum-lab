import numpy as np
import pandas as pd

df = pd.read_csv('L0.50_run1.csv')

time = df['Time (s)']
signal = df['Gyroscope z (rad/s)']

dt = np.mean(np.diff(time))
frequencies = np.fft.rfftfreq(len(signal), d=dt)
fft_spectrum = np.abs(np.fft.rfft(signal - signal.mean()))

dominant_freq = frequencies[1 + np.argmax(fft_spectrum[1:])]
period = 1 / dominant_freq

# Ruler-measured physical length
L = 0.50
L_err = 0.01

g = (4 * np.pi**2 * L) / (period**2)

print("Period (s):", period)
print("Calculated g (m/s^2):", g)
