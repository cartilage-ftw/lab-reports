import pandas as pd
import matplotlib.pyplot as plt
import numpy as np
from scipy.optimize import curve_fit

def linear_func(x, m, c):
	return m*x + c

data = pd.read_csv('opticaldata.csv', sep=',')

fig, axes = plt.subplots(figsize=(12, 6), nrows=1, ncols=2, sharex=True)
#plt.plot(data['Wavelength (nm)'], data['%T'], label='Transmittivity ($\%$)')

thic = 400.0e-9 # thickness is 400nm
# alpha = (1/thic) log(100/%T)
data['alpha'] = (1/thic)*np.log(100/data['%T'])
# energy in eV
data['energy (eV)'] = 1244/data['Wavelength (nm)']
# actually this column has the square of alpha hv
data['alpha hv'] = (data['alpha']*data['energy (eV)'])**2

axes[0].plot(data['energy (eV)'], data['alpha'], 'm-', label=r'$\alpha$')
axes[1].plot(data['energy (eV)'], data['alpha hv'], 'k-', label=r'$(\alpha h\nu)^2$')
plt.xlabel('Energy (eV)')

# fit a straight line into the linear region, which starts approximately at 3.55 eV
# find region in which energy > 3.55 eV
linear_data = data[data['energy (eV)'] >= 3.95]
#print(linear_data.head)
init_guess = (1e16, 1e15)
popt, pcov = curve_fit(linear_func, linear_data['energy (eV)'], linear_data['alpha hv'], p0=init_guess)
print(popt)
axes[1].plot(data['energy (eV)'], linear_func(data['energy (eV)'], *popt), 'r--', label='linear fit')
axes[1].set_ylim(0, max(data['alpha hv']))
#axes[0].set_yscale('log')
#axes[1].set_yscale('log')
plt.legend(loc='best')

#col_names = ['Wavelength (nm)', '%T']

plt.show()
