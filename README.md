# Pendulum Lab

I measured gravity (g) using a smartphone hanging on a string.

## What I Did
- Measured 5 string lengths (0.2m, 0.3m, 0.4m, 0.5m, 0.7m) with 2 runs for each length (10 CSV files total).
- Checked the rotation axes and manually set them in the `AXIS` dictionary in `analyze.py`.
- Calculated the pendulum period T using `find_peaks`.

## Results
- Fit line: T^2 = 2.60 * L + 0.39
- Calculated gravity: g = 15.20 m/s^2

## Why g is higher than 9.81 m/s^2
- My calculated gravity (15.20 m/s^2) is higher than expected.
- Looking at the plot, the two runs for L=0.50m and L=0.70m gave very different period values.
- For L=0.50m, one run gave T^2 ≈ 2.0s^2 while the second run gave T^2 ≈ 0.95s^2.
- This happened because the phone was twisting during the run, so `find_peaks` picked up additional rotation noise instead of the pure pendulum period.
- These inconsistent runs pulled down the fit slope to 2.60, which caused g to be calculated higher.
