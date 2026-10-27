# DataFrame Documentation

## Shape
* **Rows:** 38995
* **Columns:** 37

## Schema Summary
```text
<class 'pandas.DataFrame'>
RangeIndex: 38995 entries, 0 to 38994
Data columns (total 37 columns):
 #   Column                 Non-Null Count  Dtype 
---  ------                 --------------  ----- 
 0   name                   38995 non-null  object
 1   fet_frame              38995 non-null  object
 2   time                   38995 non-null  object
 3   kf_positions_x         37483 non-null  object
 4   kf_positions_y         37483 non-null  object
 5   kf_velocities_x        37483 non-null  object
 6   kf_velocities_y        37483 non-null  object
 7   kf_accelerations_x     37483 non-null  object
 8   kf_accelerations_y     37483 non-null  object
 9   pupil_width            1 non-null      str   
 10  pupil_height           1 non-null      str   
 11  kf_eye_event           38995 non-null  str   
 12  psycho_timestamp       3 non-null      object
 13  psychopy_event         3 non-null      str   
 14  marker                 38995 non-null  object
 15  rep                    38995 non-null  object
 16  trial                  38995 non-null  object
 17  target_size            3 non-null      object
 18  target_pos_x           38995 non-null  object
 19  target_pos_y           38995 non-null  object
 20  fet_timestamp          3 non-null      object
 21  psycho_original        38995 non-null  object
 22  nback_positions_x      37483 non-null  object
 23  nback_positions_y      37483 non-null  object
 24  nback_velocities_x     37483 non-null  object
 25  nback_velocities_y     37483 non-null  object
 26  nback_accelerations_x  37483 non-null  object
 27  nback_accelerations_y  37483 non-null  object
 28  rf_positions_x         37483 non-null  object
 29  rf_positions_y         37483 non-null  object
 30  rf_velocities_x        37483 non-null  object
 31  rf_velocities_y        37483 non-null  object
 32  rf_accelerations_x     37483 non-null  object
 33  rf_accelerations_y     37483 non-null  object
 34  is_psychopy_event      38995 non-null  object
 35  gain                   1 non-null      str   
 36  phase                  36765 non-null  object
dtypes: object(32), str(5)
memory usage: 11.0+ MB
```

## Column Breakdown
| Column Name | Data Type | Non-Null Count | Unique Values |
| --- | --- | --- | --- |
| **name** | `object` | 38995 | 38995 |
| **fet_frame** | `object` | 38995 | 38995 |
| **time** | `object` | 38995 | 38995 |
| **kf_positions_x** | `object` | 37483 | 37463 |
| **kf_positions_y** | `object` | 37483 | 37442 |
| **kf_velocities_x** | `object` | 37483 | 36597 |
| **kf_velocities_y** | `object` | 37483 | 34326 |
| **kf_accelerations_x** | `object` | 37483 | 36793 |
| **kf_accelerations_y** | `object` | 37483 | 35001 |
| **pupil_width** | `str` | 1 | 1 |
| **pupil_height** | `str` | 1 | 1 |
| **kf_eye_event** | `str` | 38995 | 6 |
| **psycho_timestamp** | `object` | 3 | 3 |
| **psychopy_event** | `str` | 3 | 3 |
| **marker** | `object` | 38995 | 5 |
| **rep** | `object` | 38995 | 3 |
| **trial** | `object` | 38995 | 3 |
| **target_size** | `object` | 3 | 3 |
| **target_pos_x** | `object` | 38995 | 3 |
| **target_pos_y** | `object` | 38995 | 3 |
| **fet_timestamp** | `object` | 3 | 3 |
| **psycho_original** | `object` | 38995 | 5 |
| **nback_positions_x** | `object` | 37483 | 37209 |
| **nback_positions_y** | `object` | 37483 | 37381 |
| **nback_velocities_x** | `object` | 37483 | 27600 |
| **nback_velocities_y** | `object` | 37483 | 33583 |
| **nback_accelerations_x** | `object` | 37483 | 30149 |
| **nback_accelerations_y** | `object` | 37483 | 34726 |
| **rf_positions_x** | `object` | 37483 | 37276 |
| **rf_positions_y** | `object` | 37483 | 37328 |
| **rf_velocities_x** | `object` | 37483 | 36427 |
| **rf_velocities_y** | `object` | 37483 | 35764 |
| **rf_accelerations_x** | `object` | 37483 | 37264 |
| **rf_accelerations_y** | `object` | 37483 | 37012 |
| **is_psychopy_event** | `object` | 38995 | 5 |
| **gain** | `str` | 1 | 1 |
| **phase** | `object` | 36765 | 6 |
