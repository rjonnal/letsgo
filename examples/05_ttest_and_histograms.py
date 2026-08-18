import letsgo as lg
import numpy as np
from matplotlib import pyplot as plt
import pandas as pd
from letsgo import plot_configuration_manuscript as pcfg
from letsgo import plotting as lgp
import scipy.stats as sps
import os,sys,glob,re

pcfg.setup()

"""This script is an example of a repeatability analysis using
intra-class correlation (ICC) and coefficient of variation (CoV)."""

# For the purposes of this example, I have downloaded data from this link:
#
# https://www.dropbox.com/scl/fi/2k4izh1cbmda43qqluw89/NeuroSleep_026.zip?rlkey=ij0txd0gwfflezlz7to2dyc8a&dl=0
#
# and I have unzipped its contents to the following location on my computer:
# /home/rjonnal/Dropbox/Data/eye_tracking/NeuroSleep_026/
# This has produced the following folder structure, relative to /home/rjonnal/Dropbox/Data/eye_tracking/

# ├── NeuroSleep_026
# │   ├── NeuroSleep_026_SD_01
# │   │   ├── 2026-07-09_13-14-14_distributional_aggregated.csv
# │   │   ├── 2026-07-09_13-14-14_drift_non_aggregated.csv
# │   │   ├── 2026-07-09_13-14-14_measurement_inform.csv
# │   │   ├── 2026-07-09_13-14-14_non_distributional_parameters.csv
# │   │   ├── 2026-07-09_13-14-14_pso_non_aggregated.csv
# │   │   ├── 2026-07-09_13-14-14_saccade_non_aggregated.csv


# assume we are interested in the Fixation_30s_PF protocol and _drift_non_aggregated files
sd_folders = glob.glob(os.path.join('/home/rjonnal/Dropbox/Data/eye_tracking/NeuroSleep_026/NeuroSleep_026_SD_0*','Fixation_30s_PF'))
sd_files = []
for sd_folder in sd_folders:
    sd_files = sd_files + glob.glob(os.path.join(sd_folder,'*_drift_non_aggregated.csv'))
    
wr_folders = glob.glob(os.path.join('/home/rjonnal/Dropbox/Data/eye_tracking/NeuroSleep_026/NeuroSleep_026_WR_0*','Fixation_30s_PF'))
wr_files = []
for wr_folder in wr_folders:
    wr_files = wr_files + glob.glob(os.path.join(wr_folder,'*_drift_non_aggregated.csv'))

# now, let's load one of the drift columns, 'drift_displacement_HV_deg_event_name'
# and compute the mean for each trial

sd_displacement_means = []
wr_displacement_means = []

for sd_file in sd_files:
    dataset = lg.Dataset(sd_file)
    dataframe = dataset.get_df()
    displacement_array = dataframe['drift_displacement_HV_deg_event_name']
    displacement_mean = float(np.mean(displacement_array))
    sd_displacement_means.append(displacement_mean)
    
for wr_file in wr_files:
    dataset = lg.Dataset(wr_file)
    dataframe = dataset.get_df()
    displacement_array = dataframe['drift_displacement_HV_deg_event_name']
    displacement_mean = float(np.mean(displacement_array))
    wr_displacement_means.append(displacement_mean)

# unpaired t-test
t_stat, p_value = sps.ttest_ind(sd_displacement_means,wr_displacement_means,equal_var=True)
print('T-test: t = %0.3f, p = %0.3f'%(t_stat,p_value))

# plot distributions
mmin = np.min(sd_displacement_means+wr_displacement_means)
mmax = np.max(sd_displacement_means+wr_displacement_means)

n_bins = 8
bin_edges = np.linspace(mmin,mmax,n_bins)
bin_lefts = bin_edges[:-1]
bin_rights = bin_edges[1:]
bin_centers = (bin_lefts+bin_rights)/2.0
bin_width = bin_edges[1]-bin_edges[0]


wr_counts,_ = np.histogram(wr_displacement_means,bin_edges)
sd_counts,_ = np.histogram(sd_displacement_means,bin_edges)

plt.bar(bin_centers,sd_counts,width=bin_width*.9,alpha=0.5,label='SD')
plt.bar(bin_centers,wr_counts,width=bin_width*.9,alpha=0.5,label='WR')
plt.ylabel('trial count')
plt.xlabel('drift displacement (deg)')
plt.legend()
plt.show()
