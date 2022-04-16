import matplotlib.pyplot as plt
import pandas as pd
import seaborn as sns

dat = pd.read_csv('readings.tsv', sep='\t', skiprows=1)
dat['V_max'] = dat['V_max'] - 5
dat['V_min'] = dat['V_min'] - 5

dat['m'] = (dat['V_max'] - dat['V_min'])/(dat['V_max'] + dat['V_min'])

dat.to_csv('reading_curated.csv', index=False)
print(dat)
