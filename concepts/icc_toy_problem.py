import pandas as pd
import pingouin as pg
import sys

# Goal: illustrate the use of ICC2 to test the reliability of some instrument when we have multiple trials
# from multiple subjects

# We will construct the DataFrame using dictionary, so let's quickly reivew how a dictionary works; a dictionary
# is a series of key-value pairs, for instance:
example_dictionary = {'pi':3.14,'e':2.72,'million':1e6}
print(example_dictionary)

# to pull a value:
print(example_dictionary['pi'])

# now our toy data

subject_id = ['S1', 'S1', 'S1', 'S2', 'S2', 'S2', 'S3', 'S3', 'S3']
trial = ['Trial_1', 'Trial_2', 'Trial_3', 'Trial_1', 'Trial_2', 'Trial_3', 'Trial_1', 'Trial_2', 'Trial_3']

# two made up data lists, one with good repeatability, one with bad
good_repeatability = [5.1,5.2,5.3,3.1,3.2,3.3,4.1,4.2,4.3]
bad_repeatability = [3.1,4.1,5.1,3.2,4.2,5.2,3.3,4.3,5.3]

tabular_data_dictionary = {
    'subject_id': subject_id,
    'trial': trial,
    'fixation_BCEA': bad_repeatability
}

# Sample dataframe: 3 subjects, each tested 3 times for fixation_BCEA
df = pd.DataFrame(tabular_data_dictionary)
print(df)
df.to_csv('toy_data.csv')

# Calculate the ICC for repeatability
# 'targets' groups by the subject, and 'raters' tracks the repeated sessions/trials
icc_results_all = pg.intraclass_corr(data=df, targets='subject_id', raters='trial', ratings='fixation_BCEA')

print(icc_results_all)

# see comment in https://github.com/raphaelvallat/pingouin/issues/485 suggesting
# that ICC2 (what we want for reliability testing) is called 'ICC(A,1)'
icc2 = icc_results_all[icc_results_all['Type']=='ICC(A,1)']

print(icc2)
