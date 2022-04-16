import matplotlib.pyplot as plt
import numpy as np
import pandas as pd

data = pd.read_csv('data.csv', header=1)
print(data.columns)

fig, axes = plt.subplots(1, 2, figsize=(12, 6), sharey=True)

# P = I^2 R
axes[0].minorticks_on()
axes[0].plot(data['Resistance'], data['Power (mW)'], color='gray', ls=':', marker='o', mfc='cornflowerblue',
				mec='k', mew=0.2)
axes[0].set_xscale('log')
axes[0].set_ylabel('Power (mW)')
axes[0].set_xlabel('Resistance ($\Omega$)')

axes[1].minorticks_on()
axes[1].plot(data['Current (mA)'], data['Power (mW)'], color='gray', ls='--', marker='D', mfc='deeppink',
			 mec='k', mew=0.2)
axes[1].set_xlabel('Current (mA)')

plt.show()
