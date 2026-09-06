# Pendulum Lab

Simple pendulum experiment using smartphone gyroscope data.

## Methodology
- **Length Measurement**: String length (L) is measured manually using a tape measure (uncertainty L_err = 0.01 m or 1 cm).
- **Period Extraction**: FFT is applied to the z-axis gyroscope data to extract the dominant oscillation frequency and compute the period (T).

## Files
- exp.py: Plots 3-axis gyroscope time series data.
- analyze.py: Computes FFT, extracts dominant period T, and calculates g.
- L0.50_run1.csv: Initial test dataset with ruler-measured L = 0.50 m.
