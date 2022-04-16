import pandas as pd
import matplotlib.pyplot as plt
import numpy as np

"""
Author: Aayush Arya
"""
data = pd.read_csv('ruby_michelson.tsv', sep='\t', header=1)

print(data.columns)

true_wav = 694e-9 # nm

data_clean = data.dropna()
print(data_clean)

wav_est = 2*data_clean['Diff100 (mm)']/100
wav_nm = wav_est*1e-3
del_wav = wav_nm - true_wav
print(del_wav)
print(f'Wavelength estimate = {np.average(wav_nm)} +/- {np.average(del_wav)}')

# Wavelength estimate = 704nm, with an average deviation from true value = 10nm
