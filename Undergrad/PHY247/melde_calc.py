import pandas as pd
import numpy as np

data = pd.read_csv('melde_obs.tsv', sep='\t', header=1)

length = 4.0 # metres
lin_density = 3.2e-3

velocity = np.sqrt(data['Tension']/lin_density)
dist = length/(data['Num Nodes']-1)
lamb = dist*2
freq = velocity/lamb
#print(data.head)
print('Speed:', velocity)
print('wavelength:', lamb)
print('freq:', freq)
print(f'Average Frequency = {np.average(freq)}; error = {125-np.average(freq)}')
