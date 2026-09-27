# Physics Pendulum Project: Measuring Gravity (g)

For this project, I tied my phone to a string and swung it like a pendulum at different lengths (from 0.20m to 0.70m) to calculate acceleration due to gravity ($g$). The phone recorded its motion using the Phyphox gyroscope sensor.

## Picking the Right Axis
Not every run swung along the exact same direction, and sometimes the phone spun on the string. I plotted the motion and drew each wave by hand in my lab notebook to figure out which axis ($X$, $Y$, or $Z$) had the true pendulum swing and which ones were just twisting noise.

- Axis choices for each file: see `notebook/`.

## What Went Wrong & How It Was Fixed
At first, I got crazy numbers for gravity because of a few mistakes in the script:

1. **Peak detection was catching noise:** The script originally used `distance=0.4s` in `find_peaks`. Since a pendulum period is around 1.0s to 1.6s, setting it to 0.4s made the code count high-frequency ripples as full swings. Increasing the distance to `0.8s` fixed this.
2. **Wrong axis on L0.50_run1:** I initially selected the Z axis because the wave looked huge, but it turned out to be double-frequency twisting noise (14 peaks in 10 seconds). Switching it to the Y axis gave the real swing (~7 peaks in 10 seconds).
3. **Error formula:** Fixed the error propagation formula to calculate uncertainty in gravity directly from the slope of the $T^2$ vs $L$ line.

## Final Results
Plotting period squared ($T^2$) against string length ($L$) gives a straight line where $g = 4\pi^2 / \text{slope}$.

Running `analyze.py` gives our final result and updates `gravity_fit_plot.png`.

---
*Note: AI helped me understand how find_peaks works, how to properly calculate slope uncertainty, and how to spot double-frequency twisting noise in gyroscope data.*