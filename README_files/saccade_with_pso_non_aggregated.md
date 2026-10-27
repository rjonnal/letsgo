# DataFrame Documentation

## Shape
* **Rows:** 4
* **Columns:** 57

## Schema Summary
```text
<class 'pandas.DataFrame'>
RangeIndex: 4 entries, 0 to 3
Data columns (total 57 columns):
 #   Column                        Non-Null Count  Dtype
---  ------                        --------------  -----
 0   parameter                     4 non-null      str  
 1   Unnamed: 1                    2 non-null      str  
 2   saccade+pso_avg_acc           3 non-null      str  
 3   saccade+pso_avg_acc.1         3 non-null      str  
 4   saccade+pso_avg_acc.2         3 non-null      str  
 5   saccade+pso_avg_acc_dir       3 non-null      str  
 6   saccade+pso_avg_acc_dir.1     3 non-null      str  
 7   saccade+pso_avg_vel_dir       3 non-null      str  
 8   saccade+pso_avg_vel_dir.1     3 non-null      str  
 9   saccade+pso_avg_speed         3 non-null      str  
 10  saccade+pso_avg_speed.1       3 non-null      str  
 11  saccade+pso_avg_speed.2       3 non-null      str  
 12  saccade+pso_top_bottom_amp    3 non-null      str  
 13  saccade+pso_top_bottom_amp.1  3 non-null      str  
 14  saccade+pso_top_bottom_amp.2  3 non-null      str  
 15  saccade+pso_duration          3 non-null      str  
 16  saccade+pso_displacement      3 non-null      str  
 17  saccade+pso_displacement.1    3 non-null      str  
 18  saccade+pso_displacement.2    3 non-null      str  
 19  saccade+pso_init_accuracy     3 non-null      str  
 20  saccade+pso_init_accuracy.1   3 non-null      str  
 21  saccade+pso_init_accuracy.2   3 non-null      str  
 22  saccade+pso_length            3 non-null      str  
 23  saccade+pso_length.1          3 non-null      str  
 24  saccade+pso_length.2          3 non-null      str  
 25  saccade+pso_onset_acc         3 non-null      str  
 26  saccade+pso_onset_acc.1       3 non-null      str  
 27  saccade+pso_onset_acc.2       3 non-null      str  
 28  saccade+pso_onset_acc.3       3 non-null      str  
 29  saccade+pso_offset_dec        3 non-null      str  
 30  saccade+pso_offset_dec.1      3 non-null      str  
 31  saccade+pso_offset_dec.2      3 non-null      str  
 32  saccade+pso_offset_dec.3      3 non-null      str  
 33  saccade+pso_onset_times       3 non-null      str  
 34  saccade+pso_onset_times.1     3 non-null      str  
 35  saccade+pso_onset_times.2     3 non-null      str  
 36  saccade+pso_offset_times      3 non-null      str  
 37  saccade+pso_offset_times.1    3 non-null      str  
 38  saccade+pso_offset_times.2    3 non-null      str  
 39  saccade+pso_max_velocity      3 non-null      str  
 40  saccade+pso_max_velocity.1    3 non-null      str  
 41  saccade+pso_max_velocity.2    3 non-null      str  
 42  saccade+pso_max_velocity.3    3 non-null      str  
 43  saccade+pso_efficiency        2 non-null      str  
 44  saccade+pso_efficiency.1      2 non-null      str  
 45  saccade+pso_efficiency.2      2 non-null      str  
 46  saccade+pso_direction         2 non-null      str  
 47  saccade+pso_direction.1       2 non-null      str  
 48  saccade+pso_closer_to_target  2 non-null      str  
 49  saccade+pso_trial_number      2 non-null      str  
 50  saccade+pso_type              2 non-null      str  
 51  saccade+pso_frame_start       2 non-null      str  
 52  saccade+pso_frame_end         2 non-null      str  
 53  saccade+pso_time_start        3 non-null      str  
 54  saccade+pso_time_end          3 non-null      str  
 55  patient_code                  1 non-null      str  
 56  path                          1 non-null      str  
dtypes: str(57)
memory usage: 1.9 KB
```

## Column Breakdown
| Column Name | Data Type | Non-Null Count | Unique Values |
| --- | --- | --- | --- |
| **parameter** | `str` | 4 | 4 |
| **Unnamed: 1** | `str` | 2 | 2 |
| **saccade+pso_avg_acc** | `str` | 3 | 3 |
| **saccade+pso_avg_acc.1** | `str` | 3 | 3 |
| **saccade+pso_avg_acc.2** | `str` | 3 | 3 |
| **saccade+pso_avg_acc_dir** | `str` | 3 | 3 |
| **saccade+pso_avg_acc_dir.1** | `str` | 3 | 3 |
| **saccade+pso_avg_vel_dir** | `str` | 3 | 3 |
| **saccade+pso_avg_vel_dir.1** | `str` | 3 | 3 |
| **saccade+pso_avg_speed** | `str` | 3 | 3 |
| **saccade+pso_avg_speed.1** | `str` | 3 | 3 |
| **saccade+pso_avg_speed.2** | `str` | 3 | 3 |
| **saccade+pso_top_bottom_amp** | `str` | 3 | 3 |
| **saccade+pso_top_bottom_amp.1** | `str` | 3 | 3 |
| **saccade+pso_top_bottom_amp.2** | `str` | 3 | 3 |
| **saccade+pso_duration** | `str` | 3 | 3 |
| **saccade+pso_displacement** | `str` | 3 | 3 |
| **saccade+pso_displacement.1** | `str` | 3 | 3 |
| **saccade+pso_displacement.2** | `str` | 3 | 3 |
| **saccade+pso_init_accuracy** | `str` | 3 | 3 |
| **saccade+pso_init_accuracy.1** | `str` | 3 | 3 |
| **saccade+pso_init_accuracy.2** | `str` | 3 | 3 |
| **saccade+pso_length** | `str` | 3 | 3 |
| **saccade+pso_length.1** | `str` | 3 | 3 |
| **saccade+pso_length.2** | `str` | 3 | 3 |
| **saccade+pso_onset_acc** | `str` | 3 | 3 |
| **saccade+pso_onset_acc.1** | `str` | 3 | 3 |
| **saccade+pso_onset_acc.2** | `str` | 3 | 3 |
| **saccade+pso_onset_acc.3** | `str` | 3 | 3 |
| **saccade+pso_offset_dec** | `str` | 3 | 3 |
| **saccade+pso_offset_dec.1** | `str` | 3 | 3 |
| **saccade+pso_offset_dec.2** | `str` | 3 | 3 |
| **saccade+pso_offset_dec.3** | `str` | 3 | 3 |
| **saccade+pso_onset_times** | `str` | 3 | 3 |
| **saccade+pso_onset_times.1** | `str` | 3 | 3 |
| **saccade+pso_onset_times.2** | `str` | 3 | 3 |
| **saccade+pso_offset_times** | `str` | 3 | 3 |
| **saccade+pso_offset_times.1** | `str` | 3 | 3 |
| **saccade+pso_offset_times.2** | `str` | 3 | 3 |
| **saccade+pso_max_velocity** | `str` | 3 | 3 |
| **saccade+pso_max_velocity.1** | `str` | 3 | 3 |
| **saccade+pso_max_velocity.2** | `str` | 3 | 3 |
| **saccade+pso_max_velocity.3** | `str` | 3 | 3 |
| **saccade+pso_efficiency** | `str` | 2 | 2 |
| **saccade+pso_efficiency.1** | `str` | 2 | 2 |
| **saccade+pso_efficiency.2** | `str` | 2 | 2 |
| **saccade+pso_direction** | `str` | 2 | 2 |
| **saccade+pso_direction.1** | `str` | 2 | 2 |
| **saccade+pso_closer_to_target** | `str` | 2 | 2 |
| **saccade+pso_trial_number** | `str` | 2 | 2 |
| **saccade+pso_type** | `str` | 2 | 2 |
| **saccade+pso_frame_start** | `str` | 2 | 2 |
| **saccade+pso_frame_end** | `str` | 2 | 2 |
| **saccade+pso_time_start** | `str` | 3 | 3 |
| **saccade+pso_time_end** | `str` | 3 | 3 |
| **patient_code** | `str` | 1 | 1 |
| **path** | `str` | 1 | 1 |
