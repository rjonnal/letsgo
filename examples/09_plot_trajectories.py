import letsgo as lg
import glob,os,sys
from pathlib import Path
import pandas as pd
from matplotlib import pyplot as plt
import numpy as np
import letsgo.plot_configuration_manuscript as pcfg
pcfg.setup()

"""This example illustrates how to plot trajectories."""

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

trajectory_columns = ['name', 'fet_frame', 'time', 'kf_positions_x', 'kf_positions_y',
                      'kf_velocities_x', 'kf_velocities_y', 'kf_accelerations_x',
                      'kf_accelerations_y', 'pupil_width', 'pupil_height', 'kf_eye_event',
                      'psycho_timestamp', 'psychopy_event', 'marker', 'target_size',
                      'opacity', 'opacity2', 'rep', 'trial', 'target_pos_x', 'target_pos_y',
                      'fet_timestamp', 'psycho_original', 'target_pos_exp_x',
                      'target_pos_exp_y', 'nback_positions_x', 'nback_positions_y',
                      'nback_velocities_x', 'nback_velocities_y', 'nback_accelerations_x',
                      'nback_accelerations_y', 'rf_positions_x', 'rf_positions_y',
                      'rf_velocities_x', 'rf_velocities_y', 'rf_accelerations_x',
                      'rf_accelerations_y', 'is_psychopy_event', 'gain', 'phase']

data_root = '/home/rjonnal/Dropbox/Data/eye_tracking/'
output_folder = '/home/rjonnal/Dropbox/Data/eye_tracking_figures/trajectory_plots'

os.makedirs(output_folder,exist_ok=True)

# recursively identify all trajectory files
p = Path(data_root)
trajectory_files = p.rglob('*trajectories.csv')


dmax_dict = {}
dmax_dict['Smooth_Pursuit_Slow'] = 2.0
dmax_dict['Antisaccade_horizontal_SW'] = 5.0
dmax_dict['Antisaccade_vertical_SW'] = 5.0
dmax_dict['Fixation_30s_PF'] = 1.0
dmax_dict['Lund_Circle_2deg'] = 2.0
dmax_dict['Lund_Circle_3deg'] = 3.0

for tf in trajectory_files:
    # get the corresponding measurement_inform file to determine the task
    tf_string = str(tf)
    mif = tf_string.replace('_trajectories.csv','_measurement_inform.csv')
    midf = pd.read_csv(mif)
    patient_code = midf['patient_code'].iloc[0]
    task = midf['protocol_name'].iloc[0]

    if tf_string.find('WR')>-1:
        condition = 'WR'
    elif tf_string.find('SD')>-1:
        condition = 'SD'
    else:
        condition = 'NA'
    
    ds = lg.Dataset(tf_string)
    
    tdf = ds.get_df()

    dmax = dmax_dict[task]
    
    x = np.array(tdf['kf_positions_x_deg'])
    y = np.array(tdf['kf_positions_y_deg'])
    try:
        plt.cla()
        plt.plot(x,y)
        plt.xlim((-dmax,dmax))
        plt.ylim((-dmax,dmax))
        plt.xlabel('x (deg)')
        plt.ylabel('y (deg)')
        plt.title('%s %s %s'%(task,condition,patient_code))
        outfn = os.path.join(output_folder,
                             '%s_%s_%s.png'%(task,condition,patient_code))
        plt.savefig(outfn,dpi=100)
        plt.pause(.1)
    except Exception as e:
        print(e)
