import letsgo as lg
import numpy as np
from matplotlib import pyplot as plt
import pandas as pd
from letsgo import plot_configuration_manuscript as pcfg
pcfg.setup()

"""This script illustrates how to plot parameters from individual
patients or from groups of patients averaged together."""

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


# filename of main CSV file
filename = '/home/rjonnal/Dropbox/Data/eye_tracking/NeuroSleep_026/NeuroSleep_026_SD_01/2026-07-09_13-14-14_trajectories.csv'

# create a Dataset object
ds = lg.Dataset(filename)

# get the distributional aggregated sheet but return it as
# a dictionary of statistics: MEAN, SD, MAX, etc.
df = ds.get_df()

t_s_arr = df['time_s']
x_deg_arr = df['kf_positions_x_deg']
y_deg_arr = df['kf_positions_y_deg']

plt.figure(figsize=(6.5,4))
plt.subplot(1,2,1)
plt.plot(t_s_arr,x_deg_arr,label='x')
plt.plot(t_s_arr,y_deg_arr,label='y')
plt.legend()
plt.xlabel('time (s)')
plt.ylabel('position (deg)')
plt.subplot(1,2,2)
plt.plot(x_deg_arr,y_deg_arr,color='tab:red',linestyle='-')
plt.xlabel('x position (deg)')
plt.ylabel('y position (deg)')
plt.show()
