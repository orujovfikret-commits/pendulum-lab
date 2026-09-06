import pandas as pd
import matplotlib.pyplot as plt

df = pd.read_csv('L0.50_run1.csv')

plt.plot(df['Time (s)'], df['Gyroscope x (rad/s)'], label='x')
plt.plot(df['Time (s)'], df['Gyroscope y (rad/s)'], label='y')
plt.plot(df['Time (s)'], df['Gyroscope z (rad/s)'], label='z')

plt.xlabel('Time (s)')
plt.ylabel('Gyroscope (rad/s)')
plt.title('Gyroscope Data')
plt.legend()
plt.show()
