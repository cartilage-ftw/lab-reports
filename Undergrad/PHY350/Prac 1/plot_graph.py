import numpy as np
import matplotlib.pyplot as plt
from matplotlib import rc
from scipy.stats import linregress

rc('text', usetex=True)
rc('font', **{'family': 'serif', 'serif': ['Computer Modern']})

t_c = [25, 40, 55, 70, 85]
t_k = np.array(t_c) + 273.15
rho = np.array([6.2011, 5.6819, 5.2479, 4.8809, 4.5672])/100

inv_tk = 1/t_k
print(np.log(rho))

figure, ax = plt.subplots(figsize=(6,6))
ax.minorticks_on()


plt.plot(1/t_k, np.log(rho), color='gray', marker='D', ls='--', mfc='#aa00ffff', mec='black', mew=0.2, label='Ge sample')
plt.xlabel('$1/T$')
plt.ylabel(r'$\log_{e} \rho$')
plt.legend()

result = linregress(1/t_k, np.log(rho))
print('Slope', result.slope)
boltz = 1.38e-23
e_g = 2*boltz*result.slope/(1.6e-19)

print('Band gap', e_g)

plt.savefig('temp_rho_var.png', dpi=300)
plt.show()


'''log_rho = np.log(rho)
del_log_rho = []
for i in range(1, len(log_rho)):
	del_log_rho.append(log_rho[i] - log_rho[i-1])
del_1_tk = []
for i in range(1, len(inv_tk)):
	del_1_tk.append(inv_tk[i]-inv_tk[i-1])

print('d/dx=',np.array(del_log_rho)/np.array(del_1_tk))
print('Slope calculation:')
print('log rho:', np.log(rho))
print('1/t_k', 1/t_k)'''
