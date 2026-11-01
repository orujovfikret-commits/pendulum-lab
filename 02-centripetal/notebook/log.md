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
- **Manual Calculation ($\omega_{\text{avg}}$):** $\omega = \frac{4.28\text{ rad}}{3.0\text{ s}} = 1.43\text{ rad/s}$
- **Lab Note on Discrepancy:** The sensor CSV shows a medium-spin peak of **2.5 – 2.7 rad/s**, which is noticeably higher than our manual calculation.
- **Reason:** Manual timing gives the **average** angular velocity over the whole 3-second interval, whereas the sensor records the instantaneous peak velocity. Also, human stopwatch reaction delay ($\approx 0.2\text{ s}$) introduces a ~7–10% error over short 3-second trials.

### Trial 2 (R0.10_test2)
- **Stopwatch Data:** Time (t) = 2.0 s | Angle = 245° (4.28 rad)
- **Manual Calculation ($\omega_{\text{avg}}$):** $\omega = \frac{4.28\text{ rad}}{2.0\text{ s}} = 2.14\text{ rad/s}$
- **Lab Note on Comparison:** The sensor CSV medium-spin peak hits **2.0 – 2.1 rad/s**, which lines up surprisingly well with the calculated value.


### Trial 3 (R0.20_test3)
- **Data Source:** CSV average, 0–3 s window
- **Calculation ($\omega_{\text{avg}}$):** $\omega = 0.51\text{ rad/s}$ (average over the initial 3s window)
- **Lab Note on Comparison:** The sensor records the whole movement right from the start, so the numbers look a bit different from manual timing.

## 3. General Observations & Status

- **Friction Decay:** The chair slowed down naturally because of bearing friction, which gave slow-down curves on the omega-time graphs.
- **Data Processing:** Used `analyze.py` to go through the 8 valid CSVs (skipped `R0.20_test.csv` since it was just a single test run). Added time windows to cut out the manual pushing parts so I only fit the clean slow-down phase.
- **Final Results:** Plotting the fitted radii against the measured radii gave a slope of $k = 0.90 \pm 0.26$ and an intercept of $d = -0.014 \pm 0.035\text{ m}$.
- **Status:** Analysis is done, plots are saved in `plots/`, results are in `results.txt`, and everything is ready to commit.

## 4. Weekly Question: Exponential Decay Verification
- **Method:** Checked the ratio of angular velocities at equal time steps ($\omega(t + \Delta t) / \omega(t)$). If the ratio stays roughly constant, it's an exponential decay.
- **Application (`R0.20_test3` slowing down):** 
  - Checked the speed every 1 second during the slow-down phase.
  - Got ratios around $\omega_1/\omega_0 = 0.672$ and $\omega_2/\omega_1 = 0.582$.
- **Conclusion:** The two ratios are not strictly equal (the second is about 13% smaller than the first). Since we only have two ratios, this is not enough data to strictly confirm a pure exponential decay, so it is better described as a general slow-down curve rather than a proven exponential.

## 5. Answers

**How close is k to 1?**
Our calculated slope is $k = 0.90 \pm 0.26$, giving a range of 0.64 to 1.16. Since 1 falls inside this window, $k$ is consistent with 1 within our uncertainty.

**What is d, and in what unit?**
The offset is $d = -0.014 \pm 0.035\text{ m}$, measured in meters. Since the interval (-0.049 m to +0.021 m) includes 0, it is consistent with 0.

**What does d say about where the sensor is?**
Because the error margin ($\pm 0.035\text{ m}$) is bigger than $d$ itself, we can't really tell where the accelerometer chip is inside the phone. The data isn't precise enough to spot a 1–2 cm offset.