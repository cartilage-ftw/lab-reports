import matplotlib.pyplot as plt
import pandas as pd
import seaborn as sns
import numpy as np

out_dat = pd.read_csv('output_chars.tsv', sep='\t')

out_dat.replace(np.nan, 0, inplace=True)
fig, ax = plt.subplots(nrows=1, ncols=2, figsize=(12,6), sharey=True)

# pinch point
plt.axvline(x=2, ls=':', color='k', lw=1.5)

ax[1].plot(out_dat['V_DS_0'], out_dat['I_D_0']*1e6, label='$V_{GS}=0$', marker='D', mfc='cornflowerblue', ls='--', color='gray', mec='k', mew='0.2')

ax[1].plot(out_dat['V_DS_0'], out_dat['I_D_1']*1e6, label='$V_{GS}=1$', marker='s', mfc='tab:pink', ls='-.', color='gray', mec='k', mew='0.2')

ax[1].plot(out_dat['V_DS_0'], out_dat['I_D_2']*1e6, label='$V_{GS}=2$', marker='*', mfc='crimson', ls='-', color='gray', mec='k', ms=8, mew='0.2')

ax[0].minorticks_on()
ax[1].minorticks_on()
ax[0].set_ylabel("$I_D$ ($\mu$A)")
ax[0].set_xlabel("$V_{DS}$")
ax[1].set_xlabel("$V_{GS}$")

# Now for the transfer char
i_d = [400, 225, 100, 25,  0]
v_ds = [0, -0.5, -1, -1.5, -2]

for y in [400, 100, 0]:
	ax[0].axhline(y, ls=':', color='gray')

ax[0].plot(v_ds, i_d, marker='o', color='gray', mfc='royalblue', ls='-')

plt.legend()
plt.tight_layout()
plt.subplots_adjust(hspace=0, wspace=0)


plt.savefig('output_chars.png', dpi=300)

plt.show()
