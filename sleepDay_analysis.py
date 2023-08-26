import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

# Load the sleepDay_merged.csv data
df_sleep_day = pd.read_csv('/../sleepDay_merged.csv')

# Display the first few rows of the dataframe
df_sleep_day.head()

'''
dataset provides information about the sleep patterns of users. Here's a brief overview of the columns:

Id: The ID of the user.
SleepDay: The date on which the sleep data was recorded.
TotalSleepRecords: The total number of sleep records for that day.
TotalMinutesAsleep: The total number of minutes the user was asleep.
TotalTimeInBed: The total time the user spent in bed.

Summary of the data:
This dataset will allow us to analyze the sleep patterns of users, including how long they sleep on average, how often they record their sleep, and the difference between the time they spend in bed and the time they are actually asleep.
'''

# General exploration of the sleepDay_merged data
# Basic information
df_sleep_day.info()

'''
Total Entries: There are 413 entries in the dataset.
Columns: The dataset has 5 columns.
Data Types:
Id: Integer (int64)
SleepDay: Object (likely a string representation of the date)
TotalSleepRecords: Integer (int64)
TotalMinutesAsleep: Integer (int64)
TotalTimeInBed: Integer (int64)
Missing Values: There are no missing values in any of the columns.
'''

# Descriptive statistics for the sleepDay_merged data
df_sleep_day.describe()

'''
Total Entries: 413
Id:
Mean: 5.00098e+09
Standard Deviation: 2.06036e+09
Min: 1.50396e+09
Max: 8.79201e+09
TotalSleepRecords:
Mean: 1.11864
Standard Deviation: 0.345521
Min: 1
Max: 3
TotalMinutesAsleep:
Mean: 419.467 minutes (approx. 7 hours)
Standard Deviation: 118.345 minutes (approx. 2 hours)
Min: 58 minutes
Max: 796 minutes (approx. 13.3 hours)
TotalTimeInBed:
Mean: 458.639 minutes (approx. 7.6 hours)
Standard Deviation: 127.102 minutes (approx. 2.1 hours)
Min: 61 minutes
Max: 961 minutes (approx. 16 hours)

Summary:

On average, users sleep for about 7 hours, but they spend approximately 7.6 hours in bed. This indicates that there's a gap of around 0.6 hours (or 36 minutes) where users are in bed but not asleep.

The maximum time a user has spent asleep is approximately 13.3 hours, while the maximum time in bed is about 16 hours. This suggests that some users might be resting in bed without necessarily sleeping for extended periods.

The minimum sleep time recorded is 58 minutes, indicating that there might be instances where users had very short sleep durations or perhaps naps.

Most users have only one sleep record per day, but there are instances where up to 3 sleep records exist for a single day. This could be due to naps or interrupted sleep.

'''

# Checking for missing values in the sleepDay_merged data
missing_values_sleep_day = df_sleep_day.isnull().sum()
missing_values_sleep_day

'''
Id: 0 missing values
SleepDay: 0 missing values
TotalSleepRecords: 0 missing values
TotalMinutesAsleep: 0 missing values
TotalTimeInBed: 0 missing values
'''

# Visualization of the distribution of TotalMinutesAsleep and TotalTimeInBed
plt.figure(figsize=(15, 6))

# Distribution of TotalMinutesAsleep
plt.subplot(1, 2, 1)
sns.histplot(df_sleep_day['TotalMinutesAsleep'], kde=True, color='blue')
plt.title('Distribution of Total Minutes Asleep')
plt.xlabel('Total Minutes Asleep')
plt.ylabel('Frequency')

# Distribution of TotalTimeInBed
plt.subplot(1, 2, 2)
sns.histplot(df_sleep_day['TotalTimeInBed'], kde=True, color='green')
plt.title('Distribution of Total Time In Bed')
plt.xlabel('Total Time In Bed')
plt.ylabel('Frequency')

plt.tight_layout()
plt.show()

'''
1. Distribution of Total Minutes Asleep:

The distribution of total minutes asleep appears to be slightly right-skewed.
Most users tend to sleep between 400 and 500 minutes (approximately 6.7 to 8.3 hours) per day.
There are some users who sleep for less than 400 minutes (less than 6.7 hours) and a few who sleep more than 600 minutes (10 hours).

2. Distribution of Total Time In Bed:

The distribution of total time in bed is also slightly right-skewed.
Most users spend between 400 and 550 minutes (approximately 6.7 to 9.2 hours) in bed.
There are users who spend less than 400 minutes in bed and a few who spend more than 650 minutes (almost 11 hours) in bed.


Summary:
The majority of users get a sleep duration that aligns with the commonly recommended 7-9 hours for adults. However, there's a noticeable difference between the time spent asleep and the total time in bed, suggesting that some users might have difficulty falling asleep or experience interruptions during their sleep.
It's essential for Bellabeat to consider these patterns when promoting their products. For instance, features that help users understand their sleep patterns or provide recommendations for improving sleep quality could be emphasized.
'''

# Visualization of the distribution of TotalMinutesAsleep and TotalTimeInBed

plt.figure(figsize=(15, 6))

# Distribution of TotalMinutesAsleep
plt.subplot(1, 2, 1)
sns.histplot(df_sleep_day['TotalMinutesAsleep'], kde=True, bins=30, color='skyblue')
plt.title('Distribution of Total Minutes Asleep')
plt.xlabel('Total Minutes Asleep')
plt.ylabel('Frequency')

# Distribution of TotalTimeInBed
plt.subplot(1, 2, 2)
sns.histplot(df_sleep_day['TotalTimeInBed'], kde=True, bins=30, color='salmon')
plt.title('Distribution of Total Time In Bed')
plt.xlabel('Total Time In Bed')
plt.ylabel('Frequency')

plt.tight_layout()
plt.show()

'''

1. Distribution of Total Minutes Asleep:

The distribution is slightly right-skewed, indicating that most users tend to sleep for around 400 to 500 minutes (6.6 to 8.3 hours) on average.
There are a few users who sleep for less than 200 minutes (3.3 hours) or more than 700 minutes (11.6 hours), but they are outliers.

2. Distribution of Total Time In Bed:

This distribution is also slightly right-skewed.
Most users spend around 400 to 550 minutes (6.6 to 9.1 hours) in bed.
There are some users who spend less than 200 minutes (3.3 hours) or more than 800 minutes (13.3 hours) in bed, but these are exceptions.

Summary:
The majority of users have a sleep duration that aligns with the recommended 7-9 hours for adults. This suggests that most users are conscious of their sleep health and aim to achieve the recommended sleep duration.

The difference between the total time in bed and total minutes asleep might be attributed to factors like the time taken to fall asleep, waking up in the middle of the night, or lying in bed without sleeping. This difference can be an area of interest for Bellabeat, as understanding and improving sleep efficiency can be a potential feature or recommendation in their products.

The outliers in both distributions could represent individuals with sleep disorders, irregular sleep patterns, or those who do not wear their device to bed every night.

'''



