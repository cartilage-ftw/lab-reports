import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

grating_data = pd.read_csv('diff_grating.tsv', sep='\t', header=1)

#for reading in ['Right V1', 'Right V2', 'Left V1', 'Left V2']:
#	grating_data[f'{reading} Total'] = grating_data[f'{reading} MSR'] + (1/60)* grating_data[f'{reading} CSR']



for pos in ['Left', 'Right']:
	grating_data[f'{pos} V1 Diff'] = abs(grating_data[f'{pos} V1 MSR'] + (1/60)*grating_data[f'{pos} V1 CSR'] - 45)
	grating_data[f'{pos} V2 Diff'] = abs(grating_data[f'{pos} V2 MSR'] + (1/60)*grating_data[f'{pos} V2 CSR'] - 135)

grating_data['Mean Angle'] = (grating_data['Right V1 Diff'] + grating_data['Right V2 Diff'] + grating_data['Left V1 Diff'] + grating_data['Left V2 Diff'])/4

print(grating_data.head)
print(grating_data['Mean Angle'])
# calibrate with green light
green_wav = 546.1e-9
green_ang = grating_data.iloc[3]['Mean Angle']
d = green_wav/np.sin(np.deg2rad(green_ang))
print('Grating constant=', d)
print('Line density=', 1/d)
line_den = 6e5 # 600 per mm = 6e5 per metre

grating_data['Wavelength'] = np.sin(np.deg2rad(grating_data['Mean Angle']))*(1/line_den)

#dispersion_power = 1*line_den/np.cos # order = 1
print(grating_data['Wavelength'])

disp_power = []

## Find d\theta/d\lambda
for i in range(1, len(grating_data)):
	dtheta = grating_data.iloc[i]['Mean Angle'] - grating_data.iloc[i-1]['Mean Angle']
	dlambda = grating_data.iloc[i]['Wavelength'] - grating_data.iloc[i-1]['Wavelength']
	ratio = dtheta/dlambda
	disp_power.append(ratio)

print('Disp power:', disp_power)
print('Average:', np.average(disp_power))

fig = plt.figure(figsize=(6,6))
plt.plot(grating_data['Wavelength'], grating_data['Mean Angle'], 'o--', color='gray', mfc='m')
plt.xlabel('Wavelength')
plt.ylabel('Diffraction Angle')
plt.show()
