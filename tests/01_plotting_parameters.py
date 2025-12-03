import letsgo as lg
import numpy as np
from matplotlib import pyplot as plt
import pandas as pd

# filename of main XLSX file
filename = '../data/Fixations-LissEyeJous001-010.xlsx'

# create a Dataset object
ds = lg.Dataset(filename)

# get the distributional aggregated sheet but return it as
# a dictionary of statistics: MEAN, SD, MAX, etc.
dfs = ds.get_split_dfs('distributional_aggregated')

mean_df = dfs['MEAN']

# list the parameters in the dataframe
for c in mean_df.columns:
    print(c)


# assume we're interested in 'drift_length;HV;deg;'
# assume we'd like to compute the mean value of this for
# each volunteer id
patient_codes = list(set(mean_df['patient_code;HV;s;']))
n_codes = len(patient_codes)



# plot all patients individually

# slice the dataframe and build the data to plot
mean_values = []
standard_deviations = []

for pc in patient_codes:
    subdf = mean_df[mean_df['patient_code;HV;s;']==pc]
    dat = subdf['drift_length;HV;deg;']
    mean_values.append(np.mean(dat))
    standard_deviations.append(np.std(dat))

patient_indices = range(len(patient_codes))
plt.figure()

plt.errorbar(patient_indices,mean_values,standard_deviations,capsize=6,linestyle='none')
plt.plot(patient_indices,mean_values,marker='s',linestyle='none')
plt.xticks(patient_indices)
plt.gca().set_xticklabels(patient_codes,rotation=45,ha='right')
plt.tight_layout()

# plot two groups of patients

group_1 = ['LissEyeJous_002', 'lisseyejous_009', 'LissEyeJous_010', 'LissEyeJous004', 'LissEyeJous007', 'LissEyejous_008']
group_2 = ['LissEyeJous005', 'LissEyeJous_001', 'LissEyeJous006', 'Jonnal_0001']

mean_values = []
standard_deviations = []
for group in [group_1,group_2]:
    subdf = []
    for patient_id in group:
        subdf.append(mean_df[mean_df['patient_code;HV;s;']==patient_id])
    subdf = pd.concat(subdf,axis=0)
    dat = subdf['drift_length;HV;deg;']
    mean_values.append(np.mean(dat))
    standard_deviations.append(np.std(dat))
    
group_names = ['group 1','group 2']
group_indices = [0,1]
plt.figure()
plt.errorbar(group_indices,mean_values,standard_deviations,capsize=6,linestyle='none')
plt.plot(group_indices,mean_values,marker='s',linestyle='none')
plt.xticks(group_indices)
plt.gca().set_xticklabels(group_names,rotation=45,ha='right')
plt.tight_layout()


plt.show()

