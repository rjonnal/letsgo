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
intra-class correlation (ICC) and coefficient of variation (CoV); it
locates all of the subjects, sessions, and trials specified, and
performs ICC analysis for every relevant task-parameter pair."""

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

# specify which sessions to analyze
sessions_to_analyze = [1,3]

# specify a minimum number of trials
minimum_trials = 2

# Reorganize session folders by task:
for folder in glob.glob(os.path.join(data_root,'NeuroSleep*')):
    for session_folder in glob.glob(os.path.join(folder,'NeuroSleep*')):
        lg.organize_by_task(session_folder,delete_old=True)

# Define a list of subject ids:
subjects = ['NeuroSleep_011','NeuroSleep_013','NeuroSleep_019','NeuroSleep_021','NeuroSleep_022','NeuroSleep_026']

# Verify that each subject folder contains sessions_to_analyze:
for subject in subjects:
    for condition_flag in ['WR','SD']:
        for session in sessions_to_analyze:
            session_string = '%02d'%session
            subject_folder = os.path.join(data_root,subject)
            session_folder = os.path.join(subject_folder, '%s_%s_%s'%(subject,condition_flag,session_string))
            assert os.path.exists(session_folder)
            
# define a condition flag to easily run this on either condition WR or SD
condition_flags = ['WR','SD']

tasks = ['Lund_Circle_2deg','Fixation_30s_PF','Smooth_Pursuit_Slow','Antisaccade_vertical_SW','Antisaccade_horizontal_SW']

parameters = ['measurement_duration_HV_s', 'trajectory_length_HV_deg', 'trajectory_length_H_deg', 'trajectory_length_V_deg', 'BCEA68_HV_deg^2', 'BCEA68_A_deg', 'BCEA95_HV_deg^2', 'BCEA98_HV_deg^2', 'P2_HV_%', 'P4_HV_%', 'fixation_stability_H_%', 'fixation_stability_V_%', 'blinks_count_HV_%', 'blinks_percentage_HV_%', 'blinks_frequency_HV_Hz', 'blinks_duration_HV_s', 'drifts_count_HV_s', 'drifts_percentage_HV_%', 'drifts_frequency_HV_Hz', 'drifts_duration_HV_s', 'saccades_count_HV_s', 'saccades_percentage_HV_%', 'saccades_frequency_HV_Hz', 'saccades_duration_HV_s', 'pso_count_HV_s', 'pso_percentage_HV_%', 'saccade+pso_frequency_HV_Hz', 'pso_duration_HV_s', 'excluded_percentage_HV_%', 'valid_data_percentage_HV_%']


def do_icc(task,parameter,condition_flag):

    # identify trials for each subject
    trials = {}
    for subject in subjects:
        trials[subject] = [] # initialize with an empty list
        subject_folder = os.path.join(data_root,subject)
        # enumerate the sessions
        #session_folders = glob.glob(os.path.join(subject_folder,'%s_%s*'%(subject,condition_flag)))

        session_folders = []
        for session in sessions_to_analyze:
            session_folders.append(os.path.join(subject_folder,'%s_%s_%02d'%(subject,condition_flag,session)))
        session_folders.sort()
        task_folders = [os.path.join(sf,task) for sf in session_folders]

        for pf in task_folders:
            trials[subject] = trials[subject] + sorted(glob.glob(os.path.join(pf,'*non_distributional_parameters.csv')))

    # for k in trials.keys():
    #     print(k)
    #     v = sorted(trials[k])
    #     for item in v:
    #         print('\t%s'%item)

    # all subjects must have the same number of trials, so we can't use all the files
    # let's determine the smallest number of trials, and limit every subject to that number
    n_trials_per_subject = [len(trials[s]) for s in subjects]
    n_trials = np.min(n_trials_per_subject)
    limiting_subject = subjects[np.argmin(n_trials_per_subject)]
    result = {}
    result['icc'] = np.nan
    result['n_trials'] = n_trials
    result['cov'] = np.nan
    
    
    try:
        assert n_trials>=minimum_trials
    except AssertionError as ae:
        print(ae)
        print('n_trials (%d) must be at least as large as minimum_trials (%d)'%(n_trials,minimum_trials))
        return result
    
    # now build the lists that will be the values in the data dataframe (see icc_toy_example.py)
    subject_rows = []
    trial_rows = []
    data_rows = []

    subject_stds = []
    subject_means = []

    for subject in subjects:
        # number the trials the same for each subject, so restart trial number
        # at 1 for each subject
        trial_number = 1
        subject_data_for_cov = []
        for csv_file in trials[subject]:
            # make a letsgo dataset for each csv file, and get the pandas dataframe
            ds = lg.Dataset(csv_file)
            df = ds.get_df()

            # extract the parameter from that file, convert to float, and make sure
            # it's not a nan
            param = df[df['parameter_axis_unit']=='value'][parameter].iloc[0]
            #print(csv_file,param)
            param = float(param)
            if np.isnan(param):
                continue

            # add the new row of data to the parallel lists
            subject_rows.append(subject)
            trial_rows.append('Trial_%03d'%trial_number)
            data_rows.append(param)
            subject_data_for_cov.append(param)
            
            trial_number+=1
            if trial_number>n_trials:
                break
        
        subject_stds.append(np.std(subject_data_for_cov))
        subject_means.append(np.mean(subject_data_for_cov))
            

    # aggregate CoVs among subjects; proposed method: RMS of stds divided by mean
    # of means, multiplied by 100%
    cov = np.sqrt(np.mean(np.array(subject_stds)**2))/np.mean(subject_means)*100.0
    
    # make a dict out of the lists of values and use this dict to make a dataframe
    data_df = pd.DataFrame({'subject':subject_rows,'trial':trial_rows,parameter:data_rows})

    # write the data_df to a csv file for visual inspection
    #data_df.to_csv('temp.csv')

    # compute the ICC
    icc_results_all = pg.intraclass_corr(data=data_df, targets='subject', raters='trial', ratings=parameter)

    # see comment in https://github.com/raphaelvallat/pingouin/issues/485 suggesting
    # that ICC2 (what we want for reliability testing) is called 'ICC(A,1)'
    icc2 = icc_results_all[icc_results_all['Type']=='ICC(A,1)']

    icc = icc2['ICC'].iloc[0]

    result['icc'] = icc
    result['cov'] = cov
    result['n_trials'] = n_trials
    
    return result


rows = []
stars = []
for task in tasks:
    for parameter in parameters:
        pair = []
        for condition_flag in condition_flags:
            print(task,parameter,condition_flag)
            res = do_icc(task, parameter, condition_flag)
            icc = res['icc']
            cov = res['cov']
            n_trials = res['n_trials']
            
            rows.append([task,parameter,condition_flag,n_trials,cov,icc])
            pair.append(icc)
        if np.min(pair)>0.6:
            stars.append('*')
            stars.append('*')
        else:
            stars.append('')
            stars.append('')
        print()
    print()

summary = pd.DataFrame(rows,columns=['task','parameter','condition','n_trials','CoV','ICC'])
summary['good'] = stars

session_string = '_'.join(['%d'%s for s in sessions_to_analyze])

summary.to_csv('summary_of_ICCs_sessions_%s.csv'%session_string)


plt.plot(summary['ICC'],summary['CoV'],'k.')
plt.ylim([0,150])
plt.xlabel('ICC(2,1)')
plt.ylabel('CoV (%)')
plt.title('Sessions: '+' '.join(['%d'%s for s in sessions_to_analyze]))
plt.savefig('CoV_vs_ICC_%s.png'%session_string)
plt.show()
