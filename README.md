# Pendulum Lab

Simple pendulum experiment using smartphone gyroscope data.

## Physics
g = (4 * pi^2 * L) / T^2

## Setup
- Length L = 0.50 m
- Period T calculated from FFT on z-axis gyroscope data

## Current Status
- Measured period T = 0.92 s, yielding calculated g ~ 23.6 m/s^2.
- The expected period for L = 0.50 m is 1.42 s (0.705 Hz), which is missing from the FFT spectrum.
- The 1.0-1.1 Hz peak suggests non-planar motion (torsional rotation or conical pendulum).
- Multi-length measurements (5 lengths, 10 runs) with rigid phone fixing are required to resolve the anomaly.

## Files
- exp.py: Plots raw gyroscope data
- analyze.py: Finds period T and calculates g
- L0.50_run1.csv: Sensor dataset
