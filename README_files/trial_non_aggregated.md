# DataFrame Documentation

## Shape
* **Rows:** 5
* **Columns:** 22

## Schema Summary
```text
<class 'pandas.DataFrame'>
RangeIndex: 5 entries, 0 to 4
Data columns (total 22 columns):
 #   Column                     Non-Null Count  Dtype
---  ------                     --------------  -----
 0   parameter                  5 non-null      str  
 1   Unnamed: 1                 3 non-null      str  
 2   saccade_init_latency       2 non-null      str  
 3   saccadic_intrusions_count  3 non-null      str  
 4   saccade_is_error           3 non-null      str  
 5   gaze_circumference         2 non-null      str  
 6   mean_gain                  1 non-null      str  
 7   std_gain                   1 non-null      str  
 8   circumference_ratio        1 non-null      str  
 9   pursuit_init_latency       2 non-null      str  
 10  mean_phase                 2 non-null      str  
 11  avg_pupil_diameters        2 non-null      str  
 12  avg_pupil_diameters.1      2 non-null      str  
 13  BCEA68                     2 non-null      str  
 14  BCEA68.1                   2 non-null      str  
 15  BCEA95                     2 non-null      str  
 16  BCEA98                     2 non-null      str  
 17  is_valid_trial             3 non-null      str  
 18  trial_frame_start          3 non-null      str  
 19  trial_frame_end            3 non-null      str  
 20  patient_code               2 non-null      str  
 21  path                       2 non-null      str  
dtypes: str(22)
memory usage: 1012.0 bytes
```

## Column Breakdown
| Column Name | Data Type | Non-Null Count | Unique Values |
| --- | --- | --- | --- |
| **parameter** | `str` | 5 | 5 |
| **Unnamed: 1** | `str` | 3 | 2 |
| **saccade_init_latency** | `str` | 2 | 2 |
| **saccadic_intrusions_count** | `str` | 3 | 3 |
| **saccade_is_error** | `str` | 3 | 2 |
| **gaze_circumference** | `str` | 2 | 2 |
| **mean_gain** | `str` | 1 | 1 |
| **std_gain** | `str` | 1 | 1 |
| **circumference_ratio** | `str` | 1 | 1 |
| **pursuit_init_latency** | `str` | 2 | 2 |
| **mean_phase** | `str` | 2 | 2 |
| **avg_pupil_diameters** | `str` | 2 | 2 |
| **avg_pupil_diameters.1** | `str` | 2 | 2 |
| **BCEA68** | `str` | 2 | 2 |
| **BCEA68.1** | `str` | 2 | 2 |
| **BCEA95** | `str` | 2 | 2 |
| **BCEA98** | `str` | 2 | 2 |
| **is_valid_trial** | `str` | 3 | 2 |
| **trial_frame_start** | `str` | 3 | 3 |
| **trial_frame_end** | `str` | 3 | 3 |
| **patient_code** | `str` | 2 | 1 |
| **path** | `str` | 2 | 1 |
