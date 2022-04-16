import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

data = pd.read_csv('forward_si.tsv', sep='\t')
print(data.columns)

fig = plt.figure(figsize=(6,6))
plt.plot(data['Forward Voltage(Volt)'], data['Forward Current(mAmp)'], 'm^--')
plt.xlabel('Forward Voltage(Volt)')
plt.ylabel('Forward Current(mAmp)')
plt.show()
