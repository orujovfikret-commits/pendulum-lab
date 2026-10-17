import os
import pandas as pd
import matplotlib.pyplot as plt

os.makedirs('plots', exist_ok=True)

df = pd.read_csv('data/R0.20_test.csv')

plt.figure()
plt.plot(df['Time (s)'], df['Angular velocity (rad/s)'])
plt.title('Gyroscope')
plt.xlabel('Time')
plt.ylabel('Omega')
plt.savefig('plots/test_gyro.png')
plt.close()

plt.figure()
plt.plot(df['Time (s)'], df['Acceleration (m/s^2)'])
plt.title('Accelerometer')
plt.xlabel('Time')
plt.ylabel('Accel')
plt.savefig('plots/test_accel.png')
plt.close()

print('Done')
