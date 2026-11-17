import letsgo as lg
import config as cfg

"""This script illustrates how to get all the possible data sets
(recordings) located below a certain point in the filesystem, and
then employ a text filter to specify the experimental condition
for each. This will make it easier later on to slice the list of
Dataset objects by condition."""

datasets = lg.get_all_datasets(cfg.data_root)

# should provide a list of Dataset objects corresponding to all
# recordings found in data_root

# now iterate through and label the datasets by condition
for ds in datasets:
    loc = ds.dataset_location
    for condition in ['WR','SD']:
        if loc.find(condition)>-1:
            ds.condition = condition
    print(ds)
