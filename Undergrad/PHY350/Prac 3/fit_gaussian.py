import matplotlib.pyplot as plt
import pandas as pd
from scipy.stats import norm
import numpy as np
from astropy import modeling
from scipy.optimize import curve_fit

data = pd.read_csv('observation.tsv', sep='\t', skiprows=1)

z_dist = 2 # mm
print(data.columns)

fig, ax = plt.subplots(figsize=(6,6))
ax.minorticks_on()

# data points
plt.scatter(data['X (mm)'], data['I (mA)'], marker='.', color='cornflowerblue', label='data')

# height at 1/e of max
red_height = max(data['I (mA)'])/np.exp(1)
plt.axhline(y=red_height, ls='--', lw=1, color='gray', label='$I_0/e$')

# Gaussian fit
def gauss(x, a, x0, sigma):
	return a*np.exp(-(x-x0)**2/(2*sigma**2))

x = data['X (mm)']
y = data['I (mA)']

#gauss_model = modeling.models.Gaussian1D()
#fitter = modeling.fitting.LevMarLSQFitter()
#fitted_model = fitter(gauss_model, data['X (mm)'], data['I (mA)'])

#plt.plot(data['X (mm)'], fitted_model(data['X (mm)']), color='gray', ls='-', label='Gaussian')

plt.xlabel('X (mm)')
plt.ylabel('I (mA)')
plt.legend()
plt.tight_layout()
plt.savefig('figure.png')

spot_width = 0.135/2
num_aperture = spot_width/np.sqrt(spot_width**2 + z_dist**2)
crit_angle = np.arcsin(num_aperture)

print(f'{crit_angle}, {num_aperture}')
 
plt.show()
