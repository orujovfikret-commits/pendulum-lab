# Lab Notebook: Experiment 2 - Centripetal Motion

## 1. Experimental Run Log

| File Name | Radius Measurement Method | Chair Tilt | Spin Intensity | Notes & Observations                                          |
| :--- | :--- | :--- | :--- |:--------------------------------------------------------------|
| R0.05_test1.csv | Measured with meter stick from axis to phone center | -2° | Slow, Medium, Fast | Started the third spin when the chair hadn't stopped.         |
| R0.05_test2.csv | Measured with meter stick from axis to phone center | -2° | Slow, Medium, Fast | More power given to all three spins than R0.05_test1.         |
| R0.10_test1.csv | Measured with meter stick from axis to phone center | -2° | Slow, Medium, Fast | Everything went well.                                         |
| R0.10_test2.csv | Measured with meter stick from axis to phone center | -2° | Slow, Medium, Fast | Everything went well.                                         |
| R0.15_test1.csv | Measured with meter stick from axis to phone center | -3° | Slow, Medium, Fast | Everything went well.                                         |
| R0.15_test2.csv | Measured with meter stick from axis to phone center | -3° | Slow, Medium, Fast | Also started the third spin when the chair hadn't stopped     |
| R0.20_test.csv | Measured with meter stick from axis to phone center | -3° | Single spin | *Discarded* (Only one spin)                                   |
| R0.20_test2.csv | Measured with meter stick from axis to phone center | -3° | Slow, Medium, Fast | Everything went well.                                         |
| R0.20_test3.csv | Measured with meter stick from axis to phone center | -3° | Slow, Medium, Fast | Additional clean test run added, everything went well aswell. |

---

## 2. Manual Stopwatch vs. Sensor Data Analysis

### Trial 1 (R0.05_test1)
- **Stopwatch Data:** Time (t) = 3.0 s | Angle = 245° (4.28 rad)
- **Manual Calculation ($\omega_{	ext{avg}}$):** $\omega = \frac{4.28\text{ rad}}{3.0\text{ s}} = 1.43\text{ rad/s}$
- **Lab Note on Discrepancy:** The sensor CSV shows a medium-spin peak of **2.5 – 2.7 rad/s**, which is noticeably higher than our manual calculation.
  * *Reason:* Manual timing gives the **average** angular velocity over the whole 3-second interval, whereas the sensor records the instantaneous peak velocity. Also, human stopwatch reaction delay ($\approx 0.2\text{ s}$) introduces a ~7–10% error over short 3-second trials.

### Trial 2 (R0.10_test2)
- **Stopwatch Data:** Time (t) = 2.0 s | Angle = 245° (4.28 rad)
- **Manual Calculation ($\omega_{	ext{avg}}$):** $\omega = \frac{4.28\text{ rad}}{2.0\text{ s}} = 2.14\text{ rad/s}$
- **Lab Note on Comparison:** The sensor CSV medium-spin peak hits **2.0 – 2.1 rad/s**, which lines up surprisingly well with the calculated value.


### Trial 3 (R0.20_test3)
- **Stopwatch Data:** Time (t) = 3.0 s (manual 3s window from release)
- **Manual Calculation ($\omega_{\text{avg}}$):** $\omega = 0.51\text{ rad/s}$ (average over the initial 3s window)
- **Lab Note on Comparison:** The sensor records the whole movement right from the start, so the numbers look a bit different from our manual timing.
---

## 3. General Observations & Status

- **Friction Decay:** The chair naturally slowed down due to bearing friction, creating clean exponential decay curves on the angular velocity graphs.
- **Data Analysis Tooling:** Used a small script (`calculate_metrics.py`) to process the CSV data and verify the numbers for Trial 3.
- **Status Update:** Ready for final submission.
- **Current Standing:** Measurements done, analysis completed.

## 4. Weekly Question: Exponential Decay Verification
- **Method:** Check the ratio of angular velocities at equal time intervals ($\omega(t + \Delta t) / \omega(t) = 	ext{constant}$). If the ratio remains constant, the decay is exponential.

- **Application (R0.20_test3 slowing down):** 
  - Checked the speed every 1 second while it was slowing down.
  - The ratio between the speeds stays pretty steady ($\approx 0.76$).
  - **Conclusion:** Since the ratio doesn't change much, it confirms it's slowing down exponentially because of friction.
