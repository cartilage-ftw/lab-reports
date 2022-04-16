import matplotlib.pyplot as plt
import numpy as np
import pandas as pd

i_b = 15.35e-3 # 15.35mA, const

v_ce = [0.1, 0.2, 0.3, 0.4, 0.6, 0.8, 1.0, 1.3, 1.5, 1.9, 2.3, 2.6, 3.0]
i_c = [5.994, 11.87, 17.52, 22.85, 32.30, 39.94, 45.81, 51.83, 54.44, 57.51, 58.95, 59.48, 59.85]

'''1	0.1000	5.994
2	0.2000	11.87
3	0.3000	17.52
4	0.4000	22.85
5	0.6000	32.30
6	0.8000	39.94
7	1.000	45.81
8	1.300	51.83
9	1.500	54.44
10	1.900	57.51
11	2.300	58.95
12	2.600	59.48
13	3.000	59.85'''

fig = plt.figure(figsize=(6,6))
plt.plot(v_ce, i_c, 'm^--')
plt.xlabel(r'$V_{CE}$')
plt.ylabel('$I_C$')
plt.title("Output characteristics of a BJT, for $I_B = 15.35 mA$")
plt.show()
