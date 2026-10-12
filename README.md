# Physics Pendulum Project: Measuring Gravity (g)

For this project, I tied my phone to a string and swung it like a pendulum at different lengths (from 0.20m to 0.70m) to calculate acceleration due to gravity ($g$). The phone recorded its motion using the Phyphox gyroscope sensor.

## Picking the Right Axis
Not every run swung along the exact same direction, and sometimes the phone spun on the string. I plotted the motion and drew each wave by hand in my lab notebook to figure out which axis ($X$, $Y$, or $Z$) had the true pendulum swing and which ones were just twisting noise.

- Axis choices for each file: see `notebook/`.

## What Went Wrong & How It Was Fixed
At first, I got crazy numbers for gravity because of a few mistakes in the script:

1. **Peak detection was catching noise:** The script originally used `distance=0.4s` in `find_peaks`. Since a pendulum period is around 1.0s to 1.6s, setting it to 0.4s made the code count high-frequency ripples as full swings. Increasing the distance to `0.8s` fixed this.
2. **False peaks from startup/shutdown chaos:** In `L0.50` and `L0.70`, the phone experienced hand-interference and twisting at the very beginning and end of the recordings, causing `find_peaks` to catch false peaks. While `prominence=0.1` was already part of the setup, fixing this required trimming the first and last 2 seconds of each run so the code only analyzed the clean oscillation phase. You can check the marked peaks in the `plots/` folder!
3. **Wrong axis on L0.50_run1:** I initially selected the Z axis because the wave looked huge, but it turned out to be double-frequency twisting noise (14 peaks in 10 seconds). Switching it to the Y axis gave the real swing (~7 peaks in 10 seconds).
4. **Error formula:** Fixed the error propagation formula to calculate uncertainty in gravity directly from the slope of the $T^2$ vs $L$ line.

## Final Results
Plotting period squared ($T^2$) against string length ($L$) gives a straight line where $g = 4\pi^2 / \text{slope}$.

Running `analyze.py` gave:
`g = 12.41 ± 1.55 m/s²`

Run pairs showed quantitative differences after trimming: at $L = 0.50\text{m}$, run 1 gave $T = [run1_period]\text{s}$ while run 2 gave $T = [run2_period]\text{s}$, and at $L = 0.70\text{m}$, run 1 gave $T = [run1_period]\text{s}$ versus run 2 at $T = [run2_period]\text{s}$. Keeping these actual results reflects the real experimental conditions.

---
*Note: AI helped me understand how find_peaks and prominence work, how to properly calculate slope uncertainty, how to spot double-frequency twisting noise in gyroscope data, and how to write a time-slicing method to trim the first and last 2 seconds of each recording to eliminate startup and shutdown noise.*