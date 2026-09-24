# Pendulum Lab

I did a physics experiment with my phone tied to a string to find gravity (g).

## What I Did
- Measured 5 lengths (0.2m, 0.3m, 0.4m, 0.5m, 0.7m).
- Recorded 2 runs per length (10 CSV files total).
- Used gyroscope data with peak detection (`find_peaks`) to measure period T without assuming g = 9.81.

## Results
- Formula line: T^2 = 3.68 * L + 0.17
- Calculated gravity: g = 10.73 ± 0.69 m/s^2

## Why is g higher than 9.81?
1. **Wrong Axis / Double Swinging**: On secondary axes the phone tilts twice per swing (~40 m/s^2). Isolated primary rotation axis.
2. **Measurement Variances**: Length offsets vary across individual runs rather than a fixed +5 cm shift. (Note: A constant length offset changes the intercept c, but does not alter the slope m or value of g).

## Note
Cleaned up repository and restarted history on Sep 24 to untrack .venv and .idea files.
