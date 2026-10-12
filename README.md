# Physics Pendulum Project: Measuring Gravity ($g$)

## 1. Question
Can the acceleration due to gravity ($g$) be accurately determined by measuring the oscillation periods of a smartphone-based string pendulum at various lengths?

---

## 2. Setup
- **App & Sensor:** The Phyphox app was used to record gyroscope data (angular velocity along the $X$ or $Y$ axis) as the phone swung.
- **Pendulum Construction:** A smartphone was securely tied to a string acting as a pendulum. 
- **Length Measurement ($L$):** Lengths were measured from the suspension point (pivot) to the center of mass of the phone, ranging from $0.20\text{m}$ to $0.70\text{m}$ with two runs per length.
- **Data Processing:** A Python script (`analyze.py`) applied time-slicing (trimming startup and shutdown noise) and used peak detection (`scipy.signal.find_peaks`) to calculate the average period ($T$) for each run.

---

## 3. Data
Plotting the square of the period ($T^2$) against the string length ($L$) yields a linear relationship based on the pendulum formula $T = 2\pi \sqrt{\frac{L}{g}}$, which rearranges to $T^2 = \left(\frac{4\pi^2}{g}\right)L$.

![T^2 vs L Fit Plot](gravity_fit_plot.png)

*Note: Individual cleaned signal plots with marked peaks are stored in the `plots/` directory.*

---

## 4. Result
From the linear regression slope ($m$) of the $T^2$ vs $L$ graph, gravity was calculated using $g = \frac{4\pi^2}{m}$:

* **Calculated Value:** $g = 10.76 \pm [error] \text{ m/s}^2$
* **Standard Value:** $9.81 \text{ m/s}^2$

---

## 5. Why Not 9.81?
While the measured value is close to the theoretical standard, discrepancies arise from several experimental factors:
1. **Length Measurement Errors:** Measuring to the center of mass of a bulky object like a phone introduces small parallax or ruler errors.
2. **Non-Ideal Pivot:** The string was tied to a fixed point, which introduced minor friction and lateral slipping rather than acting as a frictionless pivot.
3. **Twisting and Multi-Axis Noise:** Even after selecting the cleanest axis ($X$ or $Y$), the phone experienced slight rotational twisting, creating secondary frequency ripples.
4. **Amplitude Effects:** The small-angle approximation ($\sin\theta \approx \theta$) assumes small release angles, but larger initial swings introduced non-linear period shifts.
5. **Air Resistance:** Drag forces continuously slow down the pendulum, subtly affecting the true period over longer runs.

---

## 6. What I'd Do Differently
- **Rigid Clamp:** Use a proper mechanical pendulum clamp instead of tying a string to a makeshift holder to completely eliminate slipping and twisting.
- **Consistent Release:** Use a mechanical trigger or holding jig to ensure the exact same release angle and zero initial twist for every single run.
- **Precise Length Tracking:** Use a laser distance measure or vernier caliper to reduce uncertainty in length measurements.

---
*Note: AI helped me understand how peak detection and prominence work, how to properly handle slope uncertainty calculations, how to spot rotational twisting noise in gyroscope data, and how to implement time-slicing to eliminate startup/shutdown chaos.*