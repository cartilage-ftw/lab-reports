import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt

#sns.set_theme()
sns.set(style='whitegrid')

dat = pd.read_csv('water_readings.tsv', sep='\t', skiprows=1)
ax = sns.lineplot(data=dat, x='t', y='T', marker='o', label='Water')
ax.set_xlabel('time (min)')
ax.set_ylabel('Temperature')

ax_m = sns.lineplot(data=dat, x='t_m', y='T_m', marker='D', label='Milk')

ax_o = sns.lineplot(data=dat, x='t_o', y='T_o', marker='*', ms=8, label='Olive oil')

plt.savefig('figure.png', dpi=150)
plt.show()
