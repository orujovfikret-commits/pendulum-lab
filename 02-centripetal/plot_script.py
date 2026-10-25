import os
import pandas as pd
import matplotlib.pyplot as plt

os.makedirs('plots', exist_ok=True)

data_dir = '02-centripetal/data' if os.path.exists('02-centripetal/data') else 'data'

files = sorted([f for f in os.listdir(data_dir) if
                f.endswith('.csv') and '_time' not in f and 'accel' not in f and 'gyro' not in f])

for filename in files:
    filepath = os.path.join(data_dir, filename)
    df = pd.read_csv(filepath)
    test_name = filename.replace('.csv', '')

    plt.figure(figsize=(8, 4))
    plt.plot(df['Time (s)'], df['Angular velocity (rad/s)'], marker='o', color='tab:blue', linewidth=1.5)
    plt.title(f'Angular Velocity - {test_name}')
    plt.xlabel('Time (s)')
    plt.ylabel('Angular Velocity (rad/s)')
    plt.grid(True)
    plt.tight_layout()
    plt.savefig(f'plots/{test_name}_gyro.png', dpi=300)
    plt.close()

    plt.figure(figsize=(8, 4))
    plt.plot(df['Time (s)'], df['Acceleration (m/s^2)'], marker='s', color='tab:red', linewidth=1.5)
    plt.title(f'Accelerometer - {test_name}')
    plt.xlabel('Time (s)')
    plt.ylabel('Acceleration (m/s²)')
    plt.grid(True)
    plt.tight_layout()
    plt.savefig(f'plots/{test_name}_accel.png', dpi=300)
    plt.close()

print('Done')
