import matplotlib.pyplot as plt
import pandas as pd
import seaborn as sns

dat = pd.read_csv('output.tsv', sep='\t')

sns.set(style='whitegrid')
#v_be = np.array([0.2, 0.4, 0.7])
#i_b = np.array([-7.08e-6, -115.26e-6, -345.11e-6])

print(dat)
#print(type(dat['I_B'].iloc[1]))
fig = plt.figure(figsize=(6,6))

#ax = sns.lineplot(data=dat, x='V_in', y='I_in', marker='o')

ax = sns.lineplot(data = dat, x='V_CE', y='I_C', marker='D')
ax.set_xlabel('$V_{CE}$', fontsize=14)
ax.set_ylabel('$I_C$', fontsize=14)
#plt.title('Input characteristics of a CE configuration npn transistor', fontsize=14)
plt.tight_layout()
#plt.yscale('log')
plt.show()
