import pandas as pd
import matplotlib.pyplot as plt


df = pd.read_csv('L0.50_run1.csv')


plt.figure(figsize=(10, 4))
plt.plot(df['Time (s)'], df['Gyroscope z (rad/s)'], color='green', label='Gyroscope z')
plt.xlabel('Time (s)')
plt.ylabel('Rotation Rate (rad/s)')
plt.title('Pendulum Oscillation Wave')
plt.grid(True)
plt.legend()
plt.show()