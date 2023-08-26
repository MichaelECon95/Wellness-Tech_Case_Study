import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

# Load the dailySteps_merged.csv data
df_daily_steps = pd.read_csv('/.../dailySteps_merged.csv')

# Display the first few rows of the dataframe
df_daily_steps.head()

'''
This dataset provides insights into the daily step count of users. It's a straightforward dataset that can help us understand the daily activity levels of users in terms of steps taken.
'''

# General exploration of the dailySteps data

# Basic information
info_steps = df_daily_steps.info()

# Descriptive statistics
desc_stats_steps = df_daily_steps.describe()

# Checking for missing values
missing_values_steps = df_daily_steps.isnull().sum()

info_steps, desc_stats_steps, missing_values_steps

'''
Basic Information:
The dataset contains 940 entries.
There are 3 columns in the dataset.
No missing values are present in any of the columns.

Descriptive Statistics:

Id: User IDs range from approximately 1.5 billion to 8.9 billion.

StepTotal: On average, users take about 7,638 steps per day. The minimum step count is 0, and the maximum step count is 36,019.

Missing Values:
There are no missing values in the dataset.

'''

# Plotting the distribution of daily steps taken by users
plt.figure(figsize=(10, 6))
sns.histplot(df_daily_steps['StepTotal'], bins=30, kde=True)
plt.title('Distribution of Daily Steps Taken by Users')
plt.xlabel('Number of Steps')
plt.ylabel('Frequency')
plt.show()

'''
The histogram showcases the distribution of daily steps taken by users:

A majority of users take between 5,000 to 10,000 steps daily, which is in line with the general recommendation of aiming for 10,000 steps a day for adults.

There's a noticeable peak around 7,500 steps, which is close to the average step count we observed earlier.
Some users have very low step counts, close to 0, indicating days of inactivity or perhaps not wearing the Fitbit device.
A few users have exceptionally high step counts, reaching up to 35,000 steps in a day.

This distribution provides insights into the activity levels of users in terms of steps taken daily. It's evident that while many users are active and achieve the recommended step count, there's a variation in activity levels, with some being highly active and others less so.

'''
