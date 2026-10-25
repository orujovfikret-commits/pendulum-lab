import pandas as pd

file_path = 'data/R0.20_test3.csv'
df = pd.read_csv(file_path)

mask_3s = (df['Time (s)'] >= 0) & (df['Time (s)'] <= 3.0)
avg_omega_3s = df.loc[mask_3s, 'Angular velocity (rad/s)'].mean()
print(f'Manual 3s window average omega: {avg_omega_3s:.2f} rad/s')

max_idx = df['Angular velocity (rad/s)'].idxmax()
decay_df = df.iloc[max_idx:].reset_index(drop=True)

t0 = decay_df.loc[0, 'Time (s)']
w0 = decay_df.loc[0, 'Angular velocity (rad/s)']

row1 = decay_df.iloc[(decay_df['Time (s)'] - (t0 + 1.0)).abs().argsort()[:1]]
row2 = decay_df.iloc[(decay_df['Time (s)'] - (t0 + 2.0)).abs().argsort()[:1]]

w1 = row1['Angular velocity (rad/s)'].values[0]
w2 = row2['Angular velocity (rad/s)'].values[0]

ratio1 = w1 / w0 if w0 != 0 else 0
ratio2 = w2 / w1 if w1 != 0 else 0
print(f'Decay Ratios: w1/w0 = {ratio1:.3f}, w2/w1 = {ratio2:.3f}')
