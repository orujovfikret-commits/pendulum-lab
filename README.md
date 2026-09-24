# Pendulum Lab

I measured gravity (g) using a smartphone hanging on a string.

## What I Did
- Measured 5 string lengths (0.2m, 0.3m, 0.4m, 0.5m, 0.7m) with 2 runs for each length (10 CSV files total).
- Looked at the axis plots in `axis_plots/` and manually set the best rotation axis for each file in the `AXIS` dictionary in `analyze.py`.
- Used `find_peaks` to get period T for each run.

## Results
- Fit line: T^2 = 3.68 * L + 0.17
- Calculated gravity: g = 10.73 ± 0.69 m/s^2

## Notes
- Length measurement has small manual errors because measuring string with a ruler by hand is not exact.
- The rotation axis is explicitly written in `analyze.py` so the code does not select axes automatically.
