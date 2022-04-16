import matplotlib.pyplot as plt
import pandas as pd
import numpy as np

data = pd.read_csv('Integrator_Circuit.csv', names=['time1', 'V_in', 'no_name', 'time2', 'V_out'], skiprows=1)

fig, axes = plt.subplots(2, 1, figsize=(6,6), sharex=True)
axes[0].minorticks_on()
axes[1].minorticks_on()
axes[0].plot(data['time1'].iloc[88:300], data['V_out'].iloc[88:300], color='deeppink', ls='--', ms=4,
				label='$V_{out}$ (integrated)')
axes[1].plot(data['time2'].iloc[88:300], data['V_in'].iloc[88:300], color='cornflowerblue', ls='-', ms=4,
			 label='$V_{in}$ (input)')
#axes[0].legend()
axes[0].set_title('Output (integrated) signal')
axes[1].set_title('Input signal')
axes[1].set_xlabel('time (s)')
axes[1].set_ylabel('Voltage')
#print(data)

plt.savefig('integrator_result.png', dpi=300)

plt.show()
