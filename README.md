# Pendulum Lab Analysis

Data processing for determining gravitational acceleration (g) using smartphone sensor data.

## Methodology & Dataset Resolution
- **L0.21_run1.csv**: Originally mislabeled as L0.50_run1.csv. FFT analysis ( \approx 0.915\text{ s}$) and manual logbook notes (.5\text{ s}$ for 10 oscillations) confirmed an actual physical length of  \approx 0.21\text{ m}$.
- **Single-Trial Limitation**: Due to data collection constraints, $ is derived directly via  = \frac{4\pi^2 L}{T^2}$ with uncertainty propagated from FFT spectral resolution ($\Delta f \approx 0.039\text{ Hz}$).

## Scripts
- **exp.py**: Plots 3-axis gyroscope data (x, y, z) to verify planar motion.
- **analyze.py**: FFT frequency extraction, period estimation, and direct calculation of $.
