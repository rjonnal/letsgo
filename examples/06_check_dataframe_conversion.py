import letsgo as lg
import glob

"""This example tests that the various types of CSV file are all
correctly converted to Pandas dataframes."""

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


# glob all the files with a particular date-time stamp, load them, and print the resulting
# dataframes, to make sure the inference of file type and skiprows is correct
files = glob.glob('/home/rjonnal/Dropbox/Data/eye_tracking/NeuroSleep_026/NeuroSleep_026_SD_01/*/2026-07-09_13-14-14*.csv')
for f in files:
    print(f)
    ds = lg.Dataset(f)
    df = ds.get_df()
    print(df.columns)
    print(df.iloc[0])
    print()
    print()
