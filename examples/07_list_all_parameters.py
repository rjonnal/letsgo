import letsgo as lg
import config as cfg
import pandas as pd

"""This script lists all of the available parameters (aggregated dependent
variables) available in a given recording."""

dataset = lg.get_all_datasets(cfg.data_root)[0]

for k in dataset.filename_dictionary.keys():
    print("'%s',"%k,end='')
print()

dataframe_keys = ['measurement_inform',
                  'saccade_non_aggregated',
                  'pso_non_aggregated',
                  'trajectories',
                  'saccade_with_pso_non_aggregated',
                  'distributional_aggregated',
                  'non_distributional_parameters',
                  'trial_non_aggregated',
                  'drift_non_aggregated']

# Per our discussion on 17 Nov 2026, we will initially only study parameters
# aggregated by Valya's software, though let's remember there may be other
# parameters of interest (e.g., Maciej Bartuzel's suggestion to look at the
# rate of change in drifts during the 30 s fixation task).
# The nine dataframes available in the dataset are listed above, and there
# are only two that contain aggregated values: distributional_aggregated and
# non_distributional_parameters. measurement_inform and trajectories do not
# have any aggregated dependent variables in them, and the others are all
# '_non_aggregated'

da_params = list(dataset.get_dataframe('distributional_aggregated').columns)
nd_params = list(dataset.get_dataframe('non_distributional_parameters').columns)

all_params = da_params + nd_params

for param in all_params:
    print(param)
