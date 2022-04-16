import matplotlib.pyplot as plt
import pandas as pd
import numpy as np
from matplotlib import rc

dat = pd.read_csv('reading.tsv', sep='\t')

# Use LaTeX and CMU Serif font.
rc('text', usetex=True)
rc('font', **{'family': 'serif', 'serif': ['Computer Modern']})


dat['ratio'] = dat['theta_0']/dat['theta_t']
dat['log'] = np.log10(dat['ratio'])

# now do slope calcs

cap = 0.8e-6 # capacitance 0.8\muF

dat.to_csv('final_table.csv', index=False)
print(dat)

## plotting

fig, ax = plt.subplots(figsize=(6,6))
ax.minorticks_on()
plt.plot(dat['t_d'], dat['log'], marker='D', color='gray', ls='-', mfc='cornflowerblue', mec='k', mew=0.2, label='data')
plt.xlabel('time', fontsize=12)
plt.ylabel(r'$\log_{10}\left(\frac{\theta_0}{\theta_t}\right)$', fontsize=12)

ax.tick_params(axis="both", labelsize=12)

plt.text(9, 0.15, '$C=0.8\mu$F', fontsize=12)
plt.tight_layout()


# now fit a straight line
from scipy.stats import linregress

def linear_func(x, m, c):
	"""
	Straight lines!
	"""
	return m*x + c

lin_fit = linregress(dat['t_d'], dat['log'])
print(lin_fit)
t_range = np.linspace(min(dat['t_d']), max(dat['t_d']), num=len(dat))
lin_fit_y = lin_fit.slope*t_range + lin_fit.intercept

# average resistance
r_avg = 1/(2.303*lin_fit.slope*cap)

plt.plot(t_range, lin_fit_y, color='gray', ls='--', label='linear fit')

print('Average resistance R =', r_avg)
plt.legend(loc='upper left', fontsize=12)
plt.savefig('prac9_plot.png', dpi=300)
plt.show()
