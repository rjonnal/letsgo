# DataFrame Documentation

## Shape
* **Rows:** 23
* **Columns:** 57

## Schema Summary
```text
<class 'pandas.DataFrame'>
RangeIndex: 23 entries, 0 to 22
Data columns (total 57 columns):
 #   Column                    Non-Null Count  Dtype
---  ------                    --------------  -----
 0   parameter                 23 non-null     str  
 1   Unnamed: 1                21 non-null     str  
 2   saccade_avg_acc           22 non-null     str  
 3   saccade_avg_acc.1         22 non-null     str  
 4   saccade_avg_acc.2         22 non-null     str  
 5   saccade_avg_acc_dir       22 non-null     str  
 6   saccade_avg_acc_dir.1     22 non-null     str  
 7   saccade_avg_vel_dir       22 non-null     str  
 8   saccade_avg_vel_dir.1     22 non-null     str  
 9   saccade_avg_speed         22 non-null     str  
 10  saccade_avg_speed.1       22 non-null     str  
 11  saccade_avg_speed.2       22 non-null     str  
 12  saccade_top_bottom_amp    22 non-null     str  
 13  saccade_top_bottom_amp.1  22 non-null     str  
 14  saccade_top_bottom_amp.2  22 non-null     str  
 15  saccade_duration          22 non-null     str  
 16  saccade_displacement      22 non-null     str  
 17  saccade_displacement.1    22 non-null     str  
 18  saccade_displacement.2    22 non-null     str  
 19  saccade_init_accuracy     22 non-null     str  
 20  saccade_init_accuracy.1   22 non-null     str  
 21  saccade_init_accuracy.2   22 non-null     str  
 22  saccade_length            22 non-null     str  
 23  saccade_length.1          22 non-null     str  
 24  saccade_length.2          22 non-null     str  
 25  saccade_onset_acc         22 non-null     str  
 26  saccade_onset_acc.1       22 non-null     str  
 27  saccade_onset_acc.2       22 non-null     str  
 28  saccade_onset_acc.3       22 non-null     str  
 29  saccade_offset_dec        22 non-null     str  
 30  saccade_offset_dec.1      22 non-null     str  
 31  saccade_offset_dec.2      22 non-null     str  
 32  saccade_offset_dec.3      22 non-null     str  
 33  saccade_onset_times       22 non-null     str  
 34  saccade_onset_times.1     22 non-null     str  
 35  saccade_onset_times.2     22 non-null     str  
 36  saccade_offset_times      22 non-null     str  
 37  saccade_offset_times.1    22 non-null     str  
 38  saccade_offset_times.2    22 non-null     str  
 39  saccade_max_velocity      22 non-null     str  
 40  saccade_max_velocity.1    22 non-null     str  
 41  saccade_max_velocity.2    22 non-null     str  
 42  saccade_max_velocity.3    22 non-null     str  
 43  saccade_efficiency        21 non-null     str  
 44  saccade_efficiency.1      21 non-null     str  
 45  saccade_efficiency.2      21 non-null     str  
 46  saccade_direction         21 non-null     str  
 47  saccade_direction.1       21 non-null     str  
 48  saccade_closer_to_target  21 non-null     str  
 49  saccade_trial_number      21 non-null     str  
 50  saccade_type              21 non-null     str  
 51  saccade_frame_start       21 non-null     str  
 52  saccade_frame_end         21 non-null     str  
 53  saccade_time_start        22 non-null     str  
 54  saccade_time_end          22 non-null     str  
 55  patient_code              20 non-null     str  
 56  path                      20 non-null     str  
dtypes: str(57)
memory usage: 10.4 KB
```

## Column Breakdown
| Column Name | Data Type | Non-Null Count | Unique Values |
| --- | --- | --- | --- |
| **parameter** | `str` | 23 | 23 |
| **Unnamed: 1** | `str` | 21 | 2 |
| **saccade_avg_acc** | `str` | 22 | 22 |
| **saccade_avg_acc.1** | `str` | 22 | 22 |
| **saccade_avg_acc.2** | `str` | 22 | 22 |
| **saccade_avg_acc_dir** | `str` | 22 | 22 |
| **saccade_avg_acc_dir.1** | `str` | 22 | 22 |
| **saccade_avg_vel_dir** | `str` | 22 | 22 |
| **saccade_avg_vel_dir.1** | `str` | 22 | 22 |
| **saccade_avg_speed** | `str` | 22 | 22 |
| **saccade_avg_speed.1** | `str` | 22 | 22 |
| **saccade_avg_speed.2** | `str` | 22 | 22 |
| **saccade_top_bottom_amp** | `str` | 22 | 22 |
| **saccade_top_bottom_amp.1** | `str` | 22 | 22 |
| **saccade_top_bottom_amp.2** | `str` | 22 | 22 |
| **saccade_duration** | `str` | 22 | 15 |
| **saccade_displacement** | `str` | 22 | 22 |
| **saccade_displacement.1** | `str` | 22 | 22 |
| **saccade_displacement.2** | `str` | 22 | 22 |
| **saccade_init_accuracy** | `str` | 22 | 22 |
| **saccade_init_accuracy.1** | `str` | 22 | 22 |
| **saccade_init_accuracy.2** | `str` | 22 | 22 |
| **saccade_length** | `str` | 22 | 22 |
| **saccade_length.1** | `str` | 22 | 22 |
| **saccade_length.2** | `str` | 22 | 22 |
| **saccade_onset_acc** | `str` | 22 | 22 |
| **saccade_onset_acc.1** | `str` | 22 | 22 |
| **saccade_onset_acc.2** | `str` | 22 | 22 |
| **saccade_onset_acc.3** | `str` | 22 | 22 |
| **saccade_offset_dec** | `str` | 22 | 22 |
| **saccade_offset_dec.1** | `str` | 22 | 22 |
| **saccade_offset_dec.2** | `str` | 22 | 22 |
| **saccade_offset_dec.3** | `str` | 22 | 22 |
| **saccade_onset_times** | `str` | 22 | 10 |
| **saccade_onset_times.1** | `str` | 22 | 11 |
| **saccade_onset_times.2** | `str` | 22 | 9 |
| **saccade_offset_times** | `str` | 22 | 12 |
| **saccade_offset_times.1** | `str` | 22 | 13 |
| **saccade_offset_times.2** | `str` | 22 | 14 |
| **saccade_max_velocity** | `str` | 22 | 22 |
| **saccade_max_velocity.1** | `str` | 22 | 22 |
| **saccade_max_velocity.2** | `str` | 22 | 22 |
| **saccade_max_velocity.3** | `str` | 22 | 22 |
| **saccade_efficiency** | `str` | 21 | 21 |
| **saccade_efficiency.1** | `str` | 21 | 21 |
| **saccade_efficiency.2** | `str` | 21 | 21 |
| **saccade_direction** | `str` | 21 | 4 |
| **saccade_direction.1** | `str` | 21 | 4 |
| **saccade_closer_to_target** | `str` | 21 | 3 |
| **saccade_trial_number** | `str` | 21 | 3 |
| **saccade_type** | `str` | 21 | 4 |
| **saccade_frame_start** | `str` | 21 | 21 |
| **saccade_frame_end** | `str` | 21 | 21 |
| **saccade_time_start** | `str` | 22 | 22 |
| **saccade_time_end** | `str` | 22 | 22 |
| **patient_code** | `str` | 20 | 1 |
| **path** | `str` | 20 | 1 |
