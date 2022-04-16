import matplotlib.pyplot as plt
import numpy as np
import pandas as pd

data = pd.read_csv('readings.tsv', sep='\t')
data['h'] = data['Total'] - 12.8520

mu_0 = 4*np.pi*1e-7
density = 1.443 # g per cc
grav = 9.81 # m s^-2

data['sus'] = 10*(2*mu_0*density*grav*data['h']/(data['B']**2)) # a factor of 10 is needed for unit conversion
print(data)

fig, ax = plt.subplots(figsize=(6,6))
ax.minorticks_on()
plt.plot((data['h'].iloc[1:])**2, data['sus'].iloc[1:], marker='*', color='gray', mfc='red', ls='-', ms=6, mec='k', mew=0.25)

print('Average $\chi$=', np.average(data['sus'].iloc[1:]))
#plt.show()
