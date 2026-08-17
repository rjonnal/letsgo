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
# │   ├── NeuroSleep_026_SD_01
# │   │   ├── 2026-07-09_13-14-14_distributional_aggregated.csv
# │   │   ├── 2026-07-09_13-14-14_drift_non_aggregated.csv
# │   │   ├── 2026-07-09_13-14-14_measurement_inform.csv
# │   │   ├── 2026-07-09_13-14-14_non_distributional_parameters.csv
# │   │   ├── 2026-07-09_13-14-14_pso_non_aggregated.csv
# │   │   ├── 2026-07-09_13-14-14_saccade_non_aggregated.csv


sd_root = '/home/rjonnal/Dropbox/Data/eye_tracking/NeuroSleep_026/NeuroSleep_026_SD_01'
wr_root = '/home/rjonnal/Dropbox/Data/eye_tracking/NeuroSleep_026/NeuroSleep_026_WR_01'


# use the measurement_inform files from the folders to determine
# the protocol, and then organize the data files by protocol
lg.organize_by_protocol(sd_root,delete_old=True)
lg.organize_by_protocol(wr_root,delete_old=True)

# assume we are interested in the Fixation_30s_PF protocol
sd_root = os.path.join(sd_root, 'Fixation_30s_PF')
wr_root = os.path.join(wr_root, 'Fixation_30s_PF')


# assume we are interested in the drift data
# we'll sort them so that we can do file-for-file comparisons later w/o
# having to check filenames
sd_drift_files = sorted(glob.glob(os.path.join(sd_root,'*drift_non_aggregated*')))
wr_drift_files = sorted(glob.glob(os.path.join(wr_root,'*drift_non_aggregated*')))


# now, let's load one of the drift columns, 'drift_displacement_HV_deg_event_name'
# and compute the mean for each trial

sd_displacement_means = []
wr_displacement_means = []

for sd_drift_file in sd_drift_files:
    dataset = lg.Dataset(sd_drift_file)
    dataframe = dataset.get_df()
    displacement_array = dataframe['drift_displacement_HV_deg_event_name']
    displacement_mean = float(np.mean(displacement_array))
    sd_displacement_means.append(displacement_mean)
    
for wr_drift_file in wr_drift_files:
    dataset = lg.Dataset(wr_drift_file)
    dataframe = dataset.get_df()
    displacement_array = dataframe['drift_displacement_HV_deg_event_name']
    displacement_mean = float(np.mean(displacement_array))
    wr_displacement_means.append(displacement_mean)

def coefficient_of_variation(arr):
    return np.std(arr)/np.mean(arr)*100.0

print('CoV (SD): ',coefficient_of_variation(sd_displacement_means))
print('CoV (WR): ',coefficient_of_variation(wr_displacement_means))

# as a sanity check let's compare the means we computed with those in the
# 'distributional_aggregated' files

sd_da_files = sorted(glob.glob(os.path.join(sd_root,'*distributional_aggregated*')))
wr_da_files = sorted(glob.glob(os.path.join(wr_root,'*distributional_aggregated*')))

for sd_da_file,sd_displacement_mean in zip(sd_da_files,sd_displacement_means):
    df = lg.Dataset(sd_da_file,skiprows=3).get_df()
    df = df[df['parameter_axis_unit']=='MEAN']
    df_displacement_mean = df['drift_displacement_HV_deg'].iloc[0]
    print('DA file: %s'%sd_da_file)
    print('mean calculated from CSV file:\t%0.4f'%sd_displacement_mean)
    print('mean pulled from DA file:\t%0.4f'%df_displacement_mean)
    print()

for wr_da_file,wr_displacement_mean in zip(wr_da_files,wr_displacement_means):
    df = lg.Dataset(wr_da_file,skiprows=3).get_df()
    df = df[df['parameter_axis_unit']=='MEAN']
    df_displacement_mean = df['drift_displacement_HV_deg'].iloc[0]
    print('DA file: %s'%wr_da_file)
    print('mean calculated from CSV file:\t%0.4f'%wr_displacement_mean)
    print('mean pulled from DA file:\t%0.4f'%df_displacement_mean)
    print()

