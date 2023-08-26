import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

# Load the minuteStepsNarrow data
df_minuteStepsNarrow = pd.read_csv('/.../minuteStepsNarrow_merged.csv')

# Display the first few rows of the dataframe
df_minuteStepsNarrow.head()

'''
index: An index or identifier for each record.
Id: User ID.
ActivityMinute: The specific minute for which the step count is recorded.
Steps: The number of steps recorded for that specific minute.

Summary of the Data:
The minuteStepsNarrow dataset provides minute-level step counts for various users. Each row represents the number of steps a user took in a specific minute.
'''

# General exploration of the minuteStepsNarrow data
# Basic information
df_minuteStepsNarrow.info()

'''
Total Entries: 1,325,580
Columns: 3
Columns:
Id (int64): User ID. There are no missing values.
ActivityMinute (object): The specific minute for which the step count is recorded. There are no missing values.
Steps (int64): The number of steps recorded for that specific minute. There are no missing values.

Summary:
The minuteStepsNarrow dataset is comprehensive, with over 1.3 million entries. It provides minute-level granularity for step counts, and there are no missing values in any of the columns.
'''

# Descriptive statistics for the minuteStepsNarrow data
df_minuteStepsNarrow['Steps'].describe()

'''
Count: 1,325,580 entries
Mean: On average, about 5.34 steps are taken per minute.
Standard Deviation: 18.13, indicating the spread of the step counts around the mean.
Minimum: 0 steps
25th Percentile: 0 steps
Median (50th Percentile): 0 steps
75th Percentile: 0 steps
Maximum: 220 steps in a minute

Summary:
A significant portion of the data has 0 steps per minute, which could indicate periods of inactivity or rest.
The maximum number of steps recorded in a minute is 220, which is quite high and might represent moments of intense activity.
The average steps per minute is around 5.34, but the median and most of the percentiles being 0 suggest that the data has many instances of inactivity, and the mean is influenced by moments of higher activity.

'''


# Checking for missing values in the minuteStepsNarrow data
df_minuteStepsNarrow.isnull().sum()

'''
Id: 0 missing values
ActivityMinute: 0 missing values
Steps: 0 missing values

'''

# Visualization: Distribution of step counts in the minuteStepsNarrow data
plt.figure(figsize=(10, 6))
sns.histplot(df_minuteStepsNarrow['Steps'], bins=50, kde=True, color='skyblue')
plt.title('Distribution of Step Counts per Minute')
plt.xlabel('Steps')
plt.ylabel('Frequency')
plt.grid(True, which='both', linestyle='--', linewidth=0.5)
plt.show()


'''
Insights from the Visualization:

High Frequency of Zero Steps: A significant portion of the data has 0 steps per minute. This could indicate periods of inactivity, rest, or perhaps the device not being worn.

Sparse High Activity: There are instances where the step count per minute is notably high, but these instances are relatively rare. This could represent moments of intense activity or exercise.

General Inactivity: The distribution is heavily right-skewed, indicating that most of the time, users are either inactive or engage in low-intensity activities.

Summary:
The visualization provides insights into the activity patterns of the users. While there are moments of high activity, a significant portion of the data indicates inactivity or very low activity. This could be useful for Bellabeat to understand user behavior and potentially develop features or reminders to encourage more consistent activity throughout the day.
'''

