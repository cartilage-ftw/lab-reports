import matplotlib.pyplot as plt
import pandas as pd
import numpy as np

from matplotlib import rc

rc('text', usetex=True)
rc('font', **{'family': 'serif', 'serif': ['Computer Modern']})

# at B = 0.4447 T
B_3 = 0.4447
v_h_3 = np.array([34.507, 43.133, 51.760, 60.378, 69.014, 77.64, 86.267])
# at B = 0.7441 T
B_5 = 0.7441
v_h_5 = np.array([57.511, 71.889, 86.267, 100.645, 115.025, 129.4, 143.778])
# hall current (in specimen)
i_h = np.linspace(2.0, 5.0, 7)

#thickness
t = 0.5e-3 # in mm
r_h_3 = (v_h_3*t)/(i_h*B_3)
r_h_5 = (v_h_5*t)/(i_h*B_5)
print('Value for hall coeff:', [r_h_3[0], r_h_5[0]])
charge=1.6e-19
carrier_conc = 1/(r_h_3*charge)
print('Carrier density=', carrier_conc)
fig = plt.figure(figsize=(6,6))
plt.plot(i_h, v_h_3, color='gray', mfc='magenta', marker='D', linestyle='--', label=r'$B=0.447 T$')
plt.plot(i_h, v_h_5, color='olive', linestyle='-.', marker='s', label=r'$B=0.7441 T$')
plt.legend()

plt.title('Material: Ge, thickness=0.5mm')
plt.xlabel('Hall current $I_H$ (mA)')
plt.ylabel('Hall voltage $V_H$ (mV)')

plt.tight_layout()

plt.savefig('hall_effect.png', dpi=300)
plt.show()
