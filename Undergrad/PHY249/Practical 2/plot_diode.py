import matplotlib.pyplot as plt

i = [0.001, 0.026, 0.216, 0.572, .990 , 1.436, 1.895, 2.362, 2.835,
	3.312, 3.792, 4.274, 4.758, 5.244, 5.731, 6.219, 6.707]

v = [1, 1.5, 2, 2.5, 3, 3.5, 4, 4.5, 5, 5.5, 6, 6.5, 7, 7.5, 8, 8.5, 9]

plt.plot(v,i,'bo-')
plt.xlabel('Applied Voltage (V)')
plt.ylabel('Current (mA)')
plt.title('Current vs. Voltage plot for a diode')
plt.show()

