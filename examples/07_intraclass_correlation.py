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
# https://www.dropbox.com/scl/fo/dl08dncibbfpl5m1np5ln/ANj4H2W49sZqP2G6Sypi1Ag?rlkey=itydnuiyruok5wyhuejrwan12&dl=0
#
# and I have unzipped its contents to the following location on my computer:
# /home/rjonnal/Dropbox/Data/eye_tracking_working/
# This has produced the following folder structure, relative to /home/rjonnal/Dropbox/Data/eye_tracking_working/

# ├── NeuroSleep_026
# │   ├── NeuroSleep_026_SD_01
# │   │   ├── 2026-07-09_13-14-14_distributional_aggregated.csv
# │   │   ├── 2026-07-09_13-14-14_drift_non_aggregated.csv
# │   │   ├── 2026-07-09_13-14-14_measurement_inform.csv
# │   │   ├── 2026-07-09_13-14-14_non_distributional_parameters.csv
# │   │   ├── 2026-07-09_13-14-14_pso_non_aggregated.csv
# │   │   ├── 2026-07-09_13-14-14_saccade_non_aggregated.csv
# ...
# ├── NeuroSleep_013
# │   ├── NeuroSleep_013_SD_01
# ...

# For this example, we'll test the reliability of well-rested measurements first,
# and then sleep-deprived measurements next. We will treat all trials independently, regardless
# of which of the three sessions they were part of.

# Let's specify the root of the data location:
data_root = '/home/rjonnal/Dropbox/Data/eye_tracking_working/'

# Reorganize session folders by protocol:
for folder in glob.glob(os.path.join(data_root,'NeuroSleep*')):
    for session_folder in glob.glob(os.path.join(folder,'NeuroSleep*')):
        lg.organize_by_protocol(session_folder,delete_old=True)

# Define a list of subject ids:
subjects = ['NeuroSleep_011','NeuroSleep_013','NeuroSleep_019','NeuroSleep_021','NeuroSleep_022','NeuroSleep_026']

# Verify that each subject folder contains 3 SD and 3 WR sessions:
for subject in subjects:
    for condition in ['WR','SD']:
        for session in [1,2,3]:
            session_string = '%02d'%session
            subject_folder = os.path.join(data_root,subject)
            session_folder = os.path.join(subject_folder, '%s_%s_%s'%(subject,condition,session_string))
            assert os.path.exists(session_folder)


# define a condition flag to easily run this on either condition WR or SD
condition_flag = 'WR'

# define the protocol of interest
protocol = 'Fixation_30s_PF'

# identify trials for each subject
trials = {}
for subject in subjects:
    trials[subject] = [] # initialize with an empty list
    subject_folder = os.path.join(data_root,subject)
    # enumerate the sessions
    session_folders = glob.glob(os.path.join(subject_folder,'%s_%s*'%(subject,condition_flag)))
    session_folders.sort()
    protocol_folders = [os.path.join(sf,protocol) for sf in session_folders]

    print(subject)
    print(protocol_folders)
    
    





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



