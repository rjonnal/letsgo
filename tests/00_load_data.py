import letsgo as lg

# filename of main XLSX file
filename = '../data/Fixations-LissEyeJous001-010.xlsx'

# create a Dataset object
ds = lg.Dataset(filename)

# if you want to return the XLSX sheet as a single dataframe
df = ds.get_df('distributional_aggregated')

# the line above is of limited value because it returns a dataframe
# with heterogeneous rows--mean, median, etc. to return each type of
# data in its own dataframe, use get_split_dfs, which returns a dictionary
# indexed by the parameter name:
dfs = ds.get_split_dfs('distributional_aggregated')
print(dfs.keys())
print(dfs['MEAN'])

mean_df = dfs['MEAN']
