import letsgo as lg
import config as cfg

"""This script illustrates how to get all the possible data sets
(recordings) located below a certain point in the filesystem."""

datasets = lg.get_all_datasets(cfg.data_root)

# should provide a list of Dataset objects corresponding to all
# recordings found in data_root

for ds in datasets:
    print(ds)
