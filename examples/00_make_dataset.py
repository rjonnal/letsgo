import letsgo as lg

"""This script illustrates how to list all the data sets
and create a Dataset object using the time stamp from one
of them."""

data_root = '/home/rjonnal/Dropbox/Data/eye_tracking/'

datasets = lg.get_all_datasets(data_root)
# should provide a list of Dataset objects corresponding to all
# recordings found in data_root


