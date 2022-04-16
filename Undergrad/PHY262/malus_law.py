import numpy as np
import matplotlib.pyplot as plt

max_intensity = 50
first_pol = 30
second_pol = np.linspace(0, 180, 19)
intensity = [37.5, 44.15, 48.49, 50, 48.49, 44.15, 37.50, 29.34, 20.66, 12.50, 5.85, 1.51, 0.0, 1.51, 5.85, 12.50, 20.66, 29.34, 37.50]

fig = plt.figure(figsize=(8,8))
plt.plot(second_pol, intensity, color='royalblue', linestyle='-', mfc='royalblue', marker='D', label=r'$\theta$')
plt.plot((second_pol - first_pol), intensity, color='gray', linestyle='--', mfc='m',  marker='D', label=r'$\phi$')
plt.hlines(y=0, xmin=-30, xmax=180, color='darkgrey', linestyle='--', label='zero intensity')
plt.xlabel('Angle (degrees)')
plt.ylabel('Intensity')
plt.legend(loc='best')
plt.title(r'$\theta$: angle of second polaroid, $\phi$: relative phase between first and second polaroids')
plt.show()
