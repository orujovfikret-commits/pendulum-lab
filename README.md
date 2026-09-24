# Pendulum Lab

I did a physics experiment with my phone tied to a string to find gravity (g).

## What I Did
- Measured 5 lengths (0.2m, 0.3m, 0.4m, 0.5m, 0.7m) with 2 runs per length (10 CSVs).
- Isolated the primary rotation axis for each recording.
- Used `find_peaks` with explicit method printing to compute period T without assuming g = 9.81.

## Results
- Fit line: T^2 = 2.96 * L + 0.32
- Calculated gravity: g = 13.34 ± 2.24 m/s^2

## Is g = 13.34 ± 2.24 m/s^2 Significantly Different from 9.81 m/s^2?
No. The absolute difference is |13.34 - 9.81| = 3.53 m/s^2, which corresponds to **1.6 sigma** (1.58 standard deviations). Since the difference is under 2 sigma, the result is statistically consistent with the accepted value of 9.81 m/s^2 within experimental uncertainty.

## Experimental Considerations
1. **Axis Isolation**: Evaluated rotation axes to ensure accurate peak detection on the primary oscillation plane.
2. **Measurement Offsets**: Length errors varied across individual runs. A constant offset shifts intercept c but does not alter slope m or g.
