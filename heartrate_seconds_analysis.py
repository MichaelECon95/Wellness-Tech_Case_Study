import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns


# Load the heartrate_seconds_merged.csv data
df_heartrate = pd.read_csv('/.../heartrate_seconds_merged.csv')

# Display the first few rows of the dataframe
df_heartrate.head()

'''
This dataset provides insights into the heart rate measurements of users, recorded every few seconds. It's a granular dataset that can help us understand the heart rate patterns of users throughout the day.
'''

# General exploration of the heartrate data
# Basic information
info_heartrate = df_heartrate.info()

# Descriptive statistics
desc_stats_heartrate = df_heartrate.describe()

# Checking for missing values
missing_values_heartrate = df_heartrate.isnull().sum()

info_heartrate, desc_stats_heartrate, missing_values_heartrate

'''
Basic Information:

The dataset contains a substantial 2,483,658 entries.
There are 3 columns in the dataset.
No missing values are present in any of the columns.

Descriptive Statistics:

Id: User IDs range from approximately 2.02 billion to 8.88 billion.

Value (Heart Rate): The average heart rate recorded is about 77.33 bpm. The minimum heart rate value is 36 bpm, and the maximum is 203 bpm. The 25th percentile is at 63 bpm, the median (50th percentile) is at 73 bpm, and the 75th percentile is at 88 bpm.

Missing Values:
There are no missing values in the dataset.
'''

# Plotting the distribution of heart rate values
plt.figure(figsize=(10, 6))
sns.histplot(df_heartrate['Value'], bins=50, kde=True)
plt.title('Distribution of Heart Rate Values')
plt.xlabel('Heart Rate (bpm)')
plt.ylabel('Frequency')
plt.show()

'''
Based on the descriptive statistics we've observed:

The average heart rate of users is around 77.33 bpm.
The heart rate values range from a relaxed 36 bpm to an intense 203 bpm.
The distribution is likely to show a peak around the average value, with fewer occurrences of extremely low or high heart rates.
Given this data, we can infer a few things:

Resting Heart Rate: The lower values, especially those around 36-60 bpm, likely represent resting heart rates. A resting heart rate can vary, but for most adults, a heart rate of 60 to 100 bpm is considered normal. Values below this range might indicate very fit individuals or periods of deep sleep.

Active Heart Rate: The higher values, especially those above 100 bpm, represent periods of activity or exercise. A heart rate of 203 bpm is quite high and might be seen during intense physical activity.

Average Activity: The peak around the average value suggests that most of the time, users have a moderate heart rate, which could be during light activities or regular daily routines.
'''
