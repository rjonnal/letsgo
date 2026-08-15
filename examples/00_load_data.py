import letsgo as lg

"""This example illustrates how to create a letsgo dataset and extract
pandas dataframes from it."""

# filename of main CSV file
filename = '../data/datasets_unmerged/2026-06-29_17-36-08_distributional_aggregated.csv'

# create a Dataset object
ds = lg.Dataset(filename,skiprows=3)

# if you want to return the CSV file as a single dataframe
df = ds.get_df()

print('Full dataframe:')
print(df)

print('MEAN row:')
print(df[df['parameter_axis_unit']=='MEAN'])
