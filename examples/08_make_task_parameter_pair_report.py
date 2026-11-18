import letsgo as lg
import config as cfg
import pandas as pd
import sys

"""This script lists all of the available parameters (aggregated dependent
variables) available in a given recording."""

datasets = lg.get_all_datasets(cfg.data_root)

# identify unique tasks
tasks = list(set([ds.task for ds in datasets]))
da_params = list(datasets[0].get_dataframe('distributional_aggregated').columns)
nd_params = list(datasets[0].get_dataframe('non_distributional_parameters').columns)
all_params = da_params + nd_params

for task in tasks:
    for param in all_params:
        print('task: %s, parameter: %s'%(task,param))

