import pandas as pd
import matplotlib.pyplot as plt

# Load available dataset
df = pd.read_csv('L0.21_run1.csv')

plt.figure(figsize=(10, 5))
plt.plot(df['Time (s)'], df['Gyroscope x (rad/s)'], label='Gyroscope x', alpha=0.7)
plt.plot(df['Time (s)'], df['Gyroscope y (rad/s)'], label='Gyroscope y', alpha=0.7)
plt.plot(df['Time (s)'], df['Gyroscope z (rad/s)'], label='Gyroscope z', linewidth=1.5)

plt.xlabel('Time (s)')
plt.ylabel('Angular Velocity (rad/s)')
plt.title('3-Axis Gyroscope Motion Data')
plt.legend()
plt.grid(True)
plt.tight_layout()
plt.show()
