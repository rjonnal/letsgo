import letsgo as lg
import pandas as pd
from matplotlib import pyplot as plt
import numpy as np
import letsgo.plot_configuration_manuscript as pcfg
import config as cfg
import os,sys,glob

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

data_root = cfg.data_root
output_folder = cfg.output_folder
os.makedirs(output_folder,exist_ok=True)

datasets = lg.get_all_datasets(data_root)


dmax_dict = {}
dmax_dict['Smooth_Pursuit_Slow'] = 2.0
dmax_dict['Antisaccade_horizontal_SW'] = 5.0
dmax_dict['Antisaccade_vertical_SW'] = 5.0
dmax_dict['Fixation_30s_PF'] = 1.0
dmax_dict['Lund_Circle_2deg'] = 2.0
dmax_dict['Lund_Circle_3deg'] = 3.0

for ds in datasets:
    tdf = ds.get_dataframe('trajectories')
    
    dmax = dmax_dict[ds.task]
    
    event_types = set(tdf['kf_eye_event_-'])
    events = []
    event_starts = []
    last_event = None
    for idx,row in tdf.iterrows():
        event = row['kf_eye_event_-']
        if event==last_event:
            continue
        else:
            events.append(event)
            event_starts.append(row['time_s'])
        last_event = event

    event_ends = event_starts[1:]+[np.inf]

    plt.cla()
    colors = {'excluded':'w','saccade':'tab:red','drift':'tab:blue','glissade':'tab:green','blink':'w'}
    
    for e,es,ee in zip(events,event_starts,event_ends):
        if e in ['excluded','blink']:
            continue
        subdf = tdf[(tdf['time_s']>=es) & (tdf['time_s']<ee)]
        x = np.array(subdf['kf_positions_x_deg'])
        y = np.array(subdf['kf_positions_y_deg'])
        color = colors[e]
        plt.plot(x,y,color=color,linestyle='-')
    plt.xlim((-dmax,dmax))
    plt.ylim((-dmax,dmax))
    plt.xlabel('x (deg)')
    plt.ylabel('y (deg)')
    plt.axis('equal')
    plt.title('%s\n%s %s %s'%(ds.task,ds.condition,ds.patient_code,ds.timestamp))
    outfn = os.path.join(output_folder,
                         '%s_%s_%s_%s.png'%(ds.task,ds.condition,ds.patient_code,ds.timestamp))
    plt.savefig(outfn,dpi=100)
    plt.pause(1)
