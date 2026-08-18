import letsgo as lg
import glob,os

"""This example illustrates how to create a letsgo dataset and extract
pandas dataframes from it."""

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


data_root = '/home/rjonnal/Dropbox/Data/eye_tracking/NeuroSleep_026/'

# folders to be reorganized:
folders = glob.glob(os.path.join(data_root,'*'))

# by default, letsgo.organize_by_protocol will preserve the disorganized
# files while creating subfolders and organizing copies of the files
for folder in folders:
    lg.organize_by_protocol(folder)

# to move the files into their subfolders and them from their previous
# disorganized location, use delete_old=True:
# for folder in folders:
#     lg.organize_by_protocol(folder,delete_old=True)
# NB: if you run this step, earlier examples (00_load_data.py and 01_plot_trajectories.py) will
# need to be modified to account for the changes in path that result from reorganization.
