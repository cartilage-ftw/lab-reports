import matplotlib.pyplot as plt
import pandas as pd
import numpy as np
import seaborn as sns

Temp = [500, 420, 350, 310, 300]
time = list(range(0, 50, 10))

dat = pd.DataFrame(data={'Temp':Temp, 'time':time})

fig, ax = plt.subplots(figsize=(6,6))
ax.minorticks_on()
# from left 350-420 = -70. from right, 310-350 = -40; average slope at t=20s is -5.5
# if x = 20 and m = -5.5. to match y=350
# 350 = -110 + c => c = 460
x_range = np.array(list(range(0, 40)))
y_range = -5.5*x_range + 460
sns.lineplot(data=dat, x='time', y='Temp', marker='o', label='data', color='cornflowerblue')
plt.plot(x_range, y_range, ls='--', color='gray', label='slope$=-5.5$')

ax.tick_params(axis='both', labelsize=12)
plt.xlabel('time (s)', fontsize=12)
plt.ylabel('Temperature (K)', fontsize=12)
plt.legend(fontsize=12)

plt.tight_layout()
plt.savefig('problem1.png', dpi=150)
plt.show()
