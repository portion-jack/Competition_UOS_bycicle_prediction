# 2022 UOS 빅데이터 알고리즘 경진대회

```
To DO
answer based on 
raw_voting_ans.csv 
ps : 1.2 made 1.602
```

## Trials
1. column => (day, week, month, year, weekend)
- regression

2. column => (day, week, month, year, weekend)
- weekend edit with pytimekr (hollydays)
- regression

3. column => (week, month, year, weekend)
- weeken edit with pytimekr
- day is too various for data so using week_of_year base

4. 



### Data

```
data
- raw data -> year, month, day, weekday
- raw data -> drop rain data, -> year, month, day, weekday -> ans
- raw data -> smooth -> year, month, day, weekday -> ans -> smooth ans 
```





```
.
├── 1_EDA
│   ├── 1_1_eda.ipynb
│   └── 2_1_eda.ipynb
├── 2_preprocessing
│   ├── 1_1_preprocessing.ipynb
│   ├── 1_2_preprocessing.ipynb
│   └── 2_preprocessing.ipynb
├── 3_modeling
│   ├── 1_1_modeling.ipynb
│   ├── 1_2_modeling.ipynb
│   └── 1_3_modeling.ipynb
├── 4_pipeline
│   └── 3_1_eda.ipynb
├── README.md
├── checker.ipynb
├── data
│   ├── final_data
│   │   ├── test_data.csv
│   │   └── train_data.csv
│   ├── final_data_v2
│   │   ├── test_data_encoded.csv
│   │   ├── test_data_encoded_25.csv
│   │   ├── train_data_encoded.csv
│   │   └── train_data_encoded_25.csv
│   ├── pps
│   │   ├── test_data.csv
│   │   ├── train_data.csv
│   │   └── train_data_cleaned.csv
│   ├── pps_v2
│   │   ├── train_data_cleaned.csv
│   │   └── train_data_cleaned_25.csv
│   ├── rain_avg.csv
│   ├── raw_data
│   │   ├── sample_submission.csv
│   │   └── train.csv
│   ├── trial
│   │   ├── ans_mix (1).csv
│   │   ├── smooth_ratio.csv
│   │   ├── voting_smooth_25.csv
│   │   ├── voting_smooth_50.csv
│   │   ├── voting_withboosts.csv
│   │   └── voting_withboosts_ratio_applied.csv
│   └── yearly_rain.csv
├── imgs
│   └── seoul_rain.png
└── time_series_smoothing.py

12 directories, 34 files
```
