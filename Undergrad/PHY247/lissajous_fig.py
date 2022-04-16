import matplotlib.pyplot as plt
import numpy as np

t = np.linspace(1, 10, 50)
w_1 = 2 # freq along x
w_2 = 1
x = np.cos(w_1*t)
y = np.cos(w_2*t)

fig = plt.figure(figsize=(6, 6))
plt.plot(x, y, color='gray', linestyle='-', mfc='m', marker='^')
plt.xlabel('x')
plt.ylabel('y')
plt.show()
