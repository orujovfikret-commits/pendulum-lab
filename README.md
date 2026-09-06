# Pendulum Lab

Simple pendulum experiment using smartphone gyroscope sensor data.

## Methodology
- **Length Measurement**: String length (L) measured with a tape measure (L = 0.50 m).
- **Period Extraction**: FFT applied to the z-axis gyroscope data to find dominant frequency and period (T).

## Current Status & Limitations
- Current dataset contains a single run (L = 0.50 m).
- The calculated g shows an experimental anomaly, highlighting that a single data point is insufficient and multi-length linear regression (T^2 vs L) is required for accurate results.

## Files
- exp.py: Plots 3-axis gyroscope time series data.
- analyze.py: Computes FFT, extracts dominant period T, and calculates g.
- L0.50_run1.csv: Gyroscope dataset for L = 0.50 m.
