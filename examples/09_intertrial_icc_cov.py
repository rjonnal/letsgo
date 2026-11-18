import letsgo as lg
import config as cfg
import pandas as pd
import sys

"""This script lists all of the available parameters (aggregated dependent
variables) available in a given recording."""

datasets = lg.get_all_datasets(cfg.data_root)

# identify unique tasks and parameters (see 07_list_all_parameters.py for explanation)
tasks = list(set([ds.task for ds in datasets]))
da_params = list(datasets[0].get_dataframe('distributional_aggregated').columns)
nd_params = list(datasets[0].get_dataframe('non_distributional_parameters').columns)
all_params = da_params + nd_params

task_param_pairs = []
for task in tasks:
    for param in all_params:
        task_param_pairs.append((task,param))

# For each task-param, determine whether we have enough trials in at least one session
# to perform the analysis.

for task in tasks:
    task_datasets = [ds for ds in datasets if ds.task==task]
    print(task_datasets)

