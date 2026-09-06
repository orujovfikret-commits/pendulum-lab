# Pendulum Lab

Simple pendulum experiment using smartphone gyroscope data.

## Physics
g = (4 * pi^2 * L) / T^2

## Setup
- Length L = 0.50 m
- Period T calculated from FFT on z-axis gyroscope data

## Files
- exp.py: Plots raw gyroscope data
- analyze.py: Finds period T and calculates g
- L0.50_run1.csv: Sensor dataset
