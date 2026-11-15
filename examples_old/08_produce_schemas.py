import glob,os,sys,io
import pandas as pd

"""This example illustrates how to create schemas for each of the CSV files. By 'schema'
I mean a text file that summarizes the contents of each CSV file."""

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

# It is possible that you have already reorganized the files, in which case the structure is a bit different.
# Make sure the file_filter below is designed correctly. It should identify all the files associated with a particular
# time stamp.

# before reorganizing:
file_filter = '/home/rjonnal/Dropbox/Data/eye_tracking/NeuroSleep_011/NeuroSleep_011_SD_01/2026-06-17_12-59-44*.csv'
# after_reorganizing:

file_filter = '/home/rjonnal/Dropbox/Data/eye_tracking_working/NeuroSleep_011/NeuroSleep_011_SD_01/Fixation_30s_PF/2026-06-17_12-59-44*.csv'

time_stamp = '2026-06-17_12-59-44'


def generate_df_documentation(df, output_filepath=None):
    # Capture df.info() as text
    buffer = io.StringIO()
    df.info(buf=buffer)
    info_str = buffer.getvalue()
    
    # Build a clean Markdown layout
    markdown_doc = f"# DataFrame Documentation\n\n"
    markdown_doc += f"## Shape\n* **Rows:** {df.shape[0]}\n* **Columns:** {df.shape[1]}\n\n"
    markdown_doc += "## Schema Summary\n```text\n" + info_str + "```\n\n"
    
    # Generate an explicit Column Metadata Table
    markdown_doc += "## Column Breakdown\n"
    markdown_doc += "| Column Name | Data Type | Non-Null Count | Unique Values |\n"
    markdown_doc += "| --- | --- | --- | --- |\n"
    
    for col in df.columns:
        dtype = df[col].dtype
        non_null = df[col].notnull().sum()
        unique_cnt = df[col].nunique()
        markdown_doc += f"| **{col}** | `{dtype}` | {non_null} | {unique_cnt} |\n"
        
    if output_filepath:
        with open(output_filepath, "w", encoding="utf-8") as f:
            f.write(markdown_doc)
            
    return markdown_doc


files = glob.glob(file_filter)

for f in files:
    froot = os.path.split(f)[1]
    froot = os.path.splitext(froot)[0]
    froot = froot.replace(time_stamp+'_','')
    froot = froot+'.md'
    
    output_file = '../README_files/%s'%froot
    df = pd.read_csv(f)
    generate_df_documentation(df,output_file)
    print('[%s](./README_files/%s)'%(froot,froot))
