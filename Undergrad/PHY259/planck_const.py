import pandas as pd
import matplotlib.pyplot as plt
import numpy as np
from scipy.optimize import curve_fit

def linear_func(x, m, c):
	return m*x + c

data = pd.read_csv('red_led_vals.txt', sep='\t', header=1)

charge = 1.6e-19
lambd = 650.0e-9
v_c = 3.0e8
planck_const = 1.908*(charge*lambd/v_c)
print(planck_const)

fig = plt.figure(figsize=(6,6))
plt.plot(data['Voltage (V)'], data['Current (mA)'], marker='^', mfc='magenta', color='gray', label='650 nm red')
plt.xlabel('Voltage (V)')
plt.ylabel('Current (mA)')
plt.legend()
plt.show()
