import letsgo as lg
import numpy as np
from matplotlib import pyplot as plt
import pandas as pd
from letsgo import plot_configuration_manuscript as pcfg
from letsgo import plotting as lgp
import scipy.stats as sps
import os,sys,glob,re
import pingouin as pg

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
#condition_flag = 'SD'

# define the protocol and parameter of interest
protocol = 'Fixation_30s_PF'
parameter = 'BCEA95_HV_deg^2'

# identify trials for each subject
trials = {}
for subject in subjects:
    trials[subject] = [] # initialize with an empty list
    subject_folder = os.path.join(data_root,subject)
    # enumerate the sessions
    session_folders = glob.glob(os.path.join(subject_folder,'%s_%s*'%(subject,condition_flag)))
    session_folders.sort()
    for f in glob.glob(os.path.join(session_folders[0],'*')):
        print("'%s',"%os.path.split(f)[1],end='')
    sys.exit()
    protocol_folders = [os.path.join(sf,protocol) for sf in session_folders]

    for pf in protocol_folders:
        trials[subject] = trials[subject] + sorted(glob.glob(os.path.join(pf,'*non_distributional_parameters.csv')))


# all subjects must have the same number of trials, so we can't use all the files
# let's determine the smallest number of trials, and limit every subject to that number
n_trials_per_subject = [len(trials[s]) for s in subjects]
n_trials = np.min(n_trials_per_subject)

# now build the lists that will be the values in the data dataframe (see icc_toy_example.py)
subject_rows = []
trial_rows = []
data_rows = []

for subject in subjects:
    # number the trials the same for each subject, so restart trial number
    # at 1 for each subject
    trial_number = 1
    for csv_file in trials[subject]:
        # make a letsgo dataset for each csv file, and get the pandas dataframe
        ds = lg.Dataset(csv_file)
        df = ds.get_df()
        # extract the parameter from that file, convert to float, and make sure
        # it's not a nan
        param = df[df['parameter_axis_unit']=='value'][parameter].iloc[0]
        param = float(param)
        if np.isnan(param):
            continue
        
        # add the new row of data to the parallel lists
        subject_rows.append(subject)
        trial_rows.append('Trial_%03d'%trial_number)
        data_rows.append(param)
        
        trial_number+=1
        if trial_number>n_trials:
            break

# make a dict out of the lists of values and use this dict to make a dataframe
data_df = pd.DataFrame({'subject':subject_rows,'trial':trial_rows,parameter:data_rows})

# write the data_df to a csv file for visual inspection
data_df.to_csv('temp.csv')

# compute the ICC
icc_results_all = pg.intraclass_corr(data=data_df, targets='subject', raters='trial', ratings=parameter)

# see comment in https://github.com/raphaelvallat/pingouin/issues/485 suggesting
# that ICC2 (what we want for reliability testing) is called 'ICC(A,1)'
icc2 = icc_results_all[icc_results_all['Type']=='ICC(A,1)']

print(float(icc2['ICC'].iloc[0]))

