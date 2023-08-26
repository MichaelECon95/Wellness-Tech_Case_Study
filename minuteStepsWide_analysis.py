import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

# Load the minuteStepsWide data
df_minuteStepsWide = pd.read_csv('/.../minuteStepsWide_merged.csv')

# Display the first few rows of the dataframe
df_minuteStepsWide.head()

'''
dataset provides the number of steps taken by users every minute within an hour. Each column represents a minute (from "Steps00" to "Steps59"), and each row represents an hour of a day for a specific user.

Summary of the Data:
Id: The ID of the user.
ActivityHour: The specific hour for which the data is recorded.
Steps00 to Steps59: The number of steps taken by the user in each minute of the hour.
'''

# General exploration of the minuteStepsWide data
# Basic information
df_minuteStepsWide.info()

'''
Total Records: 21,645
Steps Columns: The dataset contains columns for each minute of an hour, labeled as Steps00 to Steps59. Each column represents the number of steps taken in that specific minute.
Steps Data:
Mean: On average, users took around 5 steps per minute. This average is consistent across all minute columns.
Standard Deviation: The standard deviation is around 18 for most minute columns, indicating variability in the number of steps taken by users.
Minimum: The minimum value is 0 for all minute columns, indicating that there were instances where users took no steps in a given minute.
Maximum: The maximum number of steps taken in a minute is around 182-186 steps across various minute columns.

This dataset provides a granular view of the user's activity, allowing us to analyze patterns in step activity throughout the day.

'''

# Descriptive statistics for minuteStepsWide data
df_minuteStepsWide.describe()

'''
Id: Represents the unique identifier for each user.
Total records: 21,645
Mean Id: 4.83697e+09
Range: From 1.50396e+09 to 8.87769e+09
Steps00 to Steps07: Represents the number of steps taken by users in the first 8 minutes of an hour.
Total records for each minute: 21,645
Mean steps for each minute: Varies between 5.30 to 5.59 (approx.)
Minimum steps for each minute: 0
Maximum steps for each minute: Varies between 180 to 186 (approx.)
50% of the data (median) for each minute: 0 steps

From the initial statistics, it's evident that for the first 8 minutes of any given hour, a significant number of users did not record any steps (median is 0). The maximum steps recorded in any of these minutes is around 186, which indicates that some users were quite active.
'''

# Checking for missing values in the minuteStepsWide data
missing_values_steps_wide = df_minuteStepsWide.isnull().sum()
missing_values_steps_wide

'''
dataset does not have any missing values
'''

# Visualization: Distribution of steps taken by users in a specific minute (e.g., Steps00)
plt.figure(figsize=(10, 6))
sns.histplot(df_minuteStepsWide['Steps00'], bins=50, kde=True, color='skyblue')
plt.title('Distribution of Steps Taken in the First Minute (Steps00)')
plt.xlabel('Number of Steps')
plt.ylabel('Frequency')
plt.grid(True, which='both', linestyle='--', linewidth=0.5)
plt.show()

'''
Peak at 0: A significant number of users took zero steps in the first minute, indicating moments of inactivity.
Sparse Activity: Beyond the peak at zero, the distribution shows that only a few users took a higher number of steps in that minute. The majority of users took between 0 to 20 steps.
Tail: The distribution has a long tail, indicating that there were rare instances where users took a very high number of steps in just one minute.
General Observation: The distribution suggests that many users might start their activity after the first minute or have sporadic moments of activity throughout the hour.

This visualization provides a snapshot of user activity in just one minute. Analyzing such distributions for other minutes can help identify patterns or specific minutes where users are most active.
'''

# Visualization: Distribution of steps in the first 8 minutes of an hour
plt.figure(figsize=(14, 7))
for column in df_minute_steps_wide.columns[2:10]:
    sns.kdeplot(df_minute_steps_wide[column], label=column, shade=True)
plt.title('Distribution of Steps in the First 8 Minutes of an Hour')
plt.xlabel('Number of Steps')
plt.ylabel('Density')
plt.legend()
plt.grid(True)
plt.show()


'''
The above visualization showcases the distribution of steps taken by users in the first 8 minutes of any given hour. Here's a detailed breakdown:

The KDE (Kernel Density Estimation) plots for each minute overlap significantly, indicating that the distribution of steps across these minutes is quite similar.
A prominent peak is observed at 0 steps, suggesting that a significant number of users did not record any steps in these minutes. This could be due to users being inactive or not wearing their devices.
The distributions have a long tail, indicating that while most users recorded few or no steps, there are some users who were quite active and recorded a higher number of steps.
The density decreases as the number of steps increases, which is expected as fewer users would be continuously active every minute.

Summary:
The visualization provides insights into user activity patterns in the first 8 minutes of an hour. A significant portion of users seems to be inactive during these minutes, possibly indicating periods of rest or moments when the device was not worn. However, there are also users who show consistent activity, suggesting they might be engaged in some form of exercise or activity. Understanding these patterns can help Bellabeat in tailoring marketing strategies or product features to encourage more consistent activity throughout the hour.

'''