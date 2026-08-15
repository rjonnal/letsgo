import letsgo as lg
import numpy as np
from matplotlib import pyplot as plt
import pandas as pd
from letsgo import plot_configuration_manuscript as pcfg
from letsgo import plotting as lgp
import scipy.stats as sps
pcfg.setup()

"""This script illustrates how to do an unpaired t-test on
two groups of subjects for a given eye tracking parameter,
and then how to make a box plot to visualize inter-group
differences."""


# filename of main XLSX file
filename = '../data/Fixations-LissEyeJous001-010.xlsx'

# create a Dataset object
ds = lg.Dataset(filename)

# get the distributional aggregated sheet but return it as
# a dictionary of statistics: MEAN, SD, MAX, etc.
dfs = ds.get_split_dfs('distributional_aggregated')

df = dfs['MEAN']

# list the parameters in the dataframe
for c in df.columns:
    print(c)


# assume we're interested in 'drift_length;HV;deg;'
# assume we'd like to compute the mean value of this for
# each volunteer id
patient_code_column = ds.delimiter.join(['patient_code','HV','s'])
patient_codes = list(set(df[patient_code_column]))
n_codes = len(patient_codes)


# define the parameter of interest; use ds's delimiter setting
parameter_list = ['drift_length','HV','deg']
parameter_column = ds.delimiter.join(parameter_list)


# define two groups of subjects
group_1 = [
    'LissEyeJous004',
    'LissEyejous_008',
    'lisseyejous_009',
    'LissEyeJous_010',
    'LissEyeJous006'
]

group_2 = [
    'LissEyeJous007',
    'LissEyeJous005',
    'LissEyeJous_002',
    'LissEyeJous_001',
    'Jonnal_0001'
]


# let's compute the mean and std for each subject, and store them in
# dictionaries using their patient codes as keys
parameter_means = {}
parameter_stds = {}

for pc in patient_codes:
    subdf = df[df[patient_code_column]==pc]
    dat = subdf[parameter_column]
    parameter_means[pc] = np.mean(dat)
    parameter_stds[pc] = np.std(dat)


group_1_means = [parameter_means[k] for k in group_1]
group_1_stds = [parameter_stds[k] for k in group_1]
group_2_means = [parameter_means[k] for k in group_2]
group_2_stds = [parameter_stds[k] for k in group_2]

# pooled std is RMS of stds:
group_1_std = np.sqrt(np.sum(np.array(group_1_stds)**2))
group_2_std = np.sqrt(np.sum(np.array(group_2_stds)**2))

# t-test on group means:
res = sps.ttest_ind(group_1_means,group_2_means)
print('parameter %s'%ds.column_name_to_text(parameter_column))
print('T statistic = %0.2f'%res.statistic)
print('degrees of freedom = %d'%res.df)
print('p = %0.5f'%res.pvalue)

plt.figure(figsize=(3,3))
lgp.sigboxplot((group_1_means,group_2_means))
group_names = ['HD','non-HD']
plt.gca().set_xticklabels(group_names,rotation=45,ha='right')
plt.xlabel('group')
plt.ylabel(ds.column_name_to_text(parameter_column))
plt.tight_layout()
plt.show()
