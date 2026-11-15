import letsgo as lg
import glob

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


# filename of main CSV file
filename = '/home/rjonnal/Dropbox/Data/eye_tracking/NeuroSleep_026/NeuroSleep_026_SD_01/2026-07-09_13-14-14_distributional_aggregated.csv'

# create a Dataset object
ds = lg.Dataset(filename)

# if you want to return the CSV file as a single dataframe
df = ds.get_df()

print('Full dataframe:')
print(df)

# use pandas slicing to extract the row whose 'parameter_axis_unit' is 'MEAN'
print('MEAN row:')
print(df[df['parameter_axis_unit']=='MEAN'])
