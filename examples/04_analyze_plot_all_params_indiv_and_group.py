import letsgo as lg
import numpy as np
from matplotlib import pyplot as plt
import pandas as pd
from letsgo import plot_configuration_manuscript as pcfg
from letsgo import plotting as lgp
import scipy.stats as sps
import os,sys

pcfg.setup()

"""This script illustrates how to do unpaired t-tests on
two groups of subjects for all the eye tracking parameters,
and then how to make box plots to visualize inter-group
differences for all parameters."""

# filename of main XLSX file
filename = '../data/Fixations-LissEyeJous001-010.xlsx'

# create a Dataset object
ds = lg.Dataset(filename)

# get the distributional aggregated sheet but return it as
# a dictionary of statistics: MEAN, SD, MAX, etc.
dfs = ds.get_split_dfs('distributional_aggregated')

df = dfs['MEAN']

# create an output directory
output_folder = 'output_group_indiv'
figure_folder = os.path.join(output_folder,'figures')

os.makedirs(figure_folder,exist_ok=True)

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


group_1_colors = pcfg.colors[:len(group_1)]
group_2_colors = pcfg.colors[:len(group_2)]

plt.figure(figsize=(1.5,3))
y = 0
for g,gc in zip(group_1+group_2,group_1_colors+group_2_colors):
    plt.text(0,y,g,ha='left',color=gc)
    y = y-1
    if g==group_1[-1]:
        y = y - 1
plt.ylim((y-1,0))
plt.xlim((0,0.5))
plt.xticks([])
plt.yticks([])
plt.savefig(os.path.join(output_folder,'key.png'),dpi=300)




plt.figure(figsize=(6,3))

# write to a markdown file
with open(os.path.join(output_folder,'log.md'),'w') as fid:
    fid.write('\\maxdeadcycles=1000\n\n')
    fid.write('![Legend for individual markers](./key.png)\n\\newpage')
    # list the parameters in the dataframe
    for c in df.columns:
        plt.clf()

        parameter_column = c

        # assume we're interested in 'drift_length;HV;deg;'
        # assume we'd like to compute the mean value of this for
        # each volunteer id
        patient_code_column = ds.delimiter.join(['patient_code','HV','s'])
        patient_codes = list(set(df[patient_code_column]))
        n_codes = len(patient_codes)


        # let's compute the mean and std for each subject, and store them in
        # dictionaries using their patient codes as keys
        parameter_means = {}
        parameter_stds = {}


        try:
            for pc in patient_codes:
                subdf = df[df[patient_code_column]==pc]
                dat = subdf[parameter_column]
                parameter_means[pc] = np.mean(dat)
                parameter_stds[pc] = np.std(dat)


            group_1_means = np.abs([parameter_means[k] for k in group_1])
            group_1_stds = np.abs([parameter_stds[k] for k in group_1])
            group_2_means = np.abs([parameter_means[k] for k in group_2])
            group_2_stds = np.abs([parameter_stds[k] for k in group_2])

            # pooled std is RMS of stds:
            group_1_std = np.sqrt(np.sum(np.array(group_1_stds)**2))
            group_2_std = np.sqrt(np.sum(np.array(group_2_stds)**2))

            plot_basename = parameter_column.replace(ds.delimiter,'_').replace('^','').replace('/','')+'.png'
            plot_filename = os.path.join(figure_folder,plot_basename)
            md_plot_filename = os.path.join('./figures',plot_basename)
            
            # t-test on group means:
            res = sps.ttest_ind(group_1_means,group_2_means)
            #fid.write('---\n')
            #fid.write('#### parameter %s\n\n'%ds.column_name_to_text(parameter_column))
            #fid.write('*T statistic = %0.2f\n'%res.statistic)
            #fid.write('*degrees of freedom = %d\n'%res.df)
            #fid.write('*p = %0.5f\n\n'%res.pvalue)
            fid.write('![%s, p=%0.4f](%s)\n'%(ds.column_name_to_text(parameter_column),
                                              res.pvalue,
                                              md_plot_filename))
            fid.write('\n')
            group_names = ['HD','non-HD']
            plt.subplot(1,2,1)
            lgp.groupplot((group_1_means,group_2_means),
                          (group_1_stds,group_2_stds),
                          (group_1,group_2),(group_1_colors,group_2_colors))
            plt.xticks(range(len(group_names)))
            plt.gca().set_xticklabels(group_names,rotation=45,ha='right')
            plt.xlabel('group')
            plt.ylabel(ds.column_name_to_text(parameter_column,break_line=True))
            plt.xlim((-0.5,len(group_names)-0.5))
            plt.tight_layout()

            
            plt.subplot(1,2,2)
            lgp.sigboxplot((group_1_means,group_2_means))
            plt.gca().set_xticklabels(group_names,rotation=45,ha='right')
            plt.xlabel('group')
            plt.ylabel(ds.column_name_to_text(parameter_column,break_line=True))
            plt.tight_layout()
            plt.savefig(plot_filename,dpi=300)
            plt.pause(0.001)
        except TypeError as te:
            print('Could not perform analysis on column %s.'%parameter_column)
            print(te)
