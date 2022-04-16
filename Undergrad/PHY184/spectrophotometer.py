import pandas as pd
import matplotlib.pyplot as plt


data = pd.read_csv('cuso4_spectrophotometer.tsv', sep='\t', header=1)

fig = plt.figure(figsize=(6,6))
plt.plot(data['Conc'], data['Absorbance'], marker='o', mfc='royalblue', color='gray', linestyle='--', label='$CuSO_4$')

kmno4_data = pd.read_csv('kmno4_absorbance.tsv', sep='\t', header=1)
# make sure to multiply by 1e-3 while plotting in mM, as KMnO4 Concentration was in uM
plt.plot(kmno4_data['Conc (uM)']*1e-3, kmno4_data['Absorbance'], marker='D', mfc='m', color='lightgray', linestyle = '--', label='$KMnO_4$')

kcl2_data = pd.read_csv('kcl2_absorb.tsv', sep='\t', header=1)
plt.plot(kcl2_data['Conc (mM)'], kcl2_data['Absorbance'], marker='^', mfc='olive', color='darkgrey', linestyle='--', label='$KCl_2$')

cocl2_data = pd.read_csv('cocl2_absorb.tsv', sep='\t', header=1)
plt.plot(cocl2_data['Conc (mM)'], cocl2_data['Absorbance'], marker='v', mfc='deeppink', color='silver', linestyle='--', label='$CoCl_2$')

plt.xlabel('Concentration (mM)')
plt.ylabel('Absorbance')
plt.xscale('log')
plt.yscale('log')

plt.legend()
plt.show()
