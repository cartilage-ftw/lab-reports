import matplotlib.pyplot as plt
import numpy as np
import pandas as pd

v_ce = 1.0 # constant

v_be = [0.02, 0.04, 0.06, 0.08, 0.12, 0.2, 0.3, 0.4, 0.5, 0.6]
i_b = [2.058, 2.118, 2.179, 2.242, 2.374, 2.661, 3.070, 3.542, 4.085, 4.713]

fig = plt.figure(figsize=(6,6))
plt.plot(v_be, i_b, 'm^--')
plt.show()
