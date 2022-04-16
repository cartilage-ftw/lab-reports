import numpy as np
import matplotlib.pyplot as plt

v_in = np.array([0.1, 0.5, 2.0, 4.0, 10.0, 25.0])
v_out = np.array([0.198, 0.998, 3.998, 7.998, 19.998, 50.0])

fig, ax = plt.subplots(figsize=(6, 6))

ax.minorticks_on()

plt.plot(v_in, v_out, color='gray', marker='D', ls='--', mfc='cornflowerblue', mec='k', mew=0.2, label='data')
plt.xlabel('$V_{in}$ (Volts)')
plt.ylabel('$V_{out}$ (Volts)')
plt.legend()
plt.tight_layout()
plt.savefig('figure.png')
plt.show()
