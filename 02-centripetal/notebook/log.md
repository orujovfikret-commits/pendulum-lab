# Lab Notebook: Experiment 2 - Centripetal Motion

## 1. Experimental Run Log

| File Name | Radius Measurement Method | Chair Tilt | Spin Intensity | Notes & Observations |
| :--- | :--- | :--- | :--- | :--- |
| R0.05_test1.csv | Measured with meter stick from axis to phone center | -2° | Slow, Medium, Fast | Standard run *(Logged retroactively, Oct 25)* |
| R0.05_test2.csv | Measured with meter stick from axis to phone center | -2° | Slow, Medium, Fast | Repeat run *(Logged retroactively, Oct 25)* |
| R0.10_test1.csv | Measured with meter stick from axis to phone center | -2° | Slow, Medium, Fast | Standard run *(Logged retroactively, Oct 25)* |
| R0.10_test2.csv | Measured with meter stick from axis to phone center | -2° | Slow, Medium, Fast | Repeat run *(Logged retroactively, Oct 25)* |
| R0.15_test1.csv | Measured with meter stick from axis to phone center | -3° | Slow, Medium, Fast | Standard run *(Logged retroactively, Oct 25)* |
| R0.15_test2.csv | Measured with meter stick from axis to phone center | -3° | Slow, Medium, Fast | Repeat run *(Logged retroactively, Oct 25)* |
| R0.20_test.csv | Measured with meter stick from axis to phone center | -3° | Single spin | *Discarded* (Setup test only: 4.5s long, Oct 17) |
| R0.20_test2.csv | Measured with meter stick from axis to phone center | -3° | Slow, Medium, Fast | Standard run *(Logged retroactively, Oct 25)* |
| R0.20_test3.csv | Measured with meter stick from axis to phone center | -3° | Slow, Medium, Fast | Additional clean test run added |

---

## 2. Manual Stopwatch vs. Sensor Data Analysis

### Trial 1 (R0.05_test1)
- **Stopwatch Data:** Time ($) = 3.0 s | Angle ($	heta$) = 245° (4.28 rad)
- **Manual Calculation ($\omega_{	ext{avg}}$):** $\omega = \frac{4.28\text{ rad}}{3.0\text{ s}} = 1.43\text{ rad/s}$
- **Lab Note on Discrepancy:** The sensor CSV shows a medium-spin peak of **2.5 – 2.7 rad/s**, which is noticeably higher than our manual calculation.
  * *Reason:* Manual timing gives the **average** angular velocity over the whole 3-second interval, whereas the sensor records the instantaneous peak velocity. Also, human stopwatch reaction delay ($\approx 0.2\text{ s}$) introduces a ~7–10% error over short 3-second trials.

### Trial 2 (R0.10_test2)
- **Stopwatch Data:** Time ($) = 2.0 s | Angle ($	heta$) = 245° (4.28 rad)
- **Manual Calculation ($\omega_{	ext{avg}}$):** $\omega = \frac{4.28\text{ rad}}{2.0\text{ s}} = 2.14\text{ rad/s}$
- **Lab Note on Comparison:** The sensor CSV medium-spin peak hits **2.0 – 2.1 rad/s**, which lines up surprisingly well with the calculated value.

---

## 3. General Observations & Status

- **Friction Decay:** The chair naturally slows down due to bearing friction, creating clean exponential decay curves on the angular velocity graphs.
- **Status Update:** ~~Ready for final submission.~~
- **Current Standing:** Measurements done, analysis next.

## 4. Weekly Question: Exponential Decay Verification
- **Method:** Check the ratio of angular velocities at equal time intervals ($\omega(t + \Delta t) / \omega(t) = 	ext{constant}$). If the ratio remains constant, the decay is exponential.
