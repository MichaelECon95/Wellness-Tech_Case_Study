import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns


# Load the minuteMETsNarrow_merged.csv data
df_minute_METs = pd.read_csv('/.../minuteMETsNarrow_merged.csv')

# Display the first few rows of the dataframe
df_minute_METs.head()

'''
MET (Metabolic Equivalent of Task) is a physiological measure expressing the energy cost of physical activities. It represents the ratio of the rate at which a person expends energy during an activity to the rate of energy expenditure at rest. For example, 1 MET is the rate of energy expenditure while at rest, while a higher MET value indicates greater energy expenditure and thus more intense activity.

This dataset can provide insights into the energy expenditure of users during different activities.
'''

# General exploration of the minute-by-minute MET data
# Basic information
info_minute_METs = df_minute_METs.info()

# Descriptive statistics
desc_stats_minute_METs = df_minute_METs.describe()

# Checking for missing values
missing_values_minute_METs = df_minute_METs.isnull().sum()

info_minute_METs, desc_stats_minute_METs, missing_values_minute_METs

'''
Basic Information:
The dataset contains 1,325,580 entries.
There are 3 columns in the dataset.
No missing values are present in any of the columns.

Descriptive Statistics:

Id: User IDs range from approximately 1.50 billion to 8.88 billion.

METs:
The average MET value is around 14.69, indicating the average energy expenditure relative to resting.
The minimum MET value is 0, suggesting periods of rest or inactivity.
The maximum MET value is 157, indicating very high-intensity activities.
The 25th, 50th (median), and 75th percentiles are 10, 10, and 11 respectively, suggesting that most of the MET values are clustered around the lower range.

Missing Values:
There are no missing values in the dataset.
'''
# Plotting the distribution of MET values
plt.figure(figsize=(12, 6))
sns.histplot(df_minute_METs['METs'], bins=50, kde=True, color='purple')
plt.title('Distribution of MET Values')
plt.xlabel('MET Value')
plt.ylabel('Frequency')
plt.show()

'''
Insights from the MET Values Distribution:
Predominance of Low MET Values: The distribution shows a peak around the lower MET values, indicating that users often have periods of minimal activity or rest during many minutes of the day.

Sparse High MET Values: There are fewer instances of very high MET values, suggesting that very high-intensity activities are less frequent among users.

General Trend: Most users exhibit low to moderate energy expenditure for a significant portion of the day, with occasional spikes in activity leading to higher MET values.

Understanding the MET values can provide insights into the intensity and energy expenditure of users' activities. This can be valuable for Bellabeat in several ways:

Activity Recommendations: By understanding the typical MET values, Bellabeat can suggest activities that help users achieve higher MET values, promoting more calorie burn and better fitness outcomes.

Goal Setting: Users can be encouraged to set goals based on MET values, aiming to achieve higher energy expenditure levels during their workouts.

Integration with Intensity Data: By combining MET values with the previously analyzed intensity data, we can get a comprehensive view of users' activity patterns. This can help in tailoring personalized fitness plans for users.
'''

----------------------------------------------------------------------


#exploring the relationship between MET values and daily steps. This will help us understand if higher energy expenditure (as indicated by MET values) correlates with a higher number of steps taken daily.

'''
To do this, we'll:

Aggregate the MET values and steps on a daily basis for each user.
Plot a scatter plot to visualize the relationship between daily MET values and daily steps.
'''

df_daily_activity = pd.read_csv('/.../dailyActivity_merged.csv')

# Aggregating MET values and steps on a daily basis for each user
df_minute_METs['Date'] = pd.to_datetime(df_minute_METs['ActivityMinute']).dt.date
df_daily_METs = df_minute_METs.groupby(['Id', 'Date'])['METs'].sum().reset_index()
df_daily_steps = df_daily_activity[['Id', 'ActivityDate', 'TotalSteps']]
df_daily_steps['ActivityDate'] = pd.to_datetime(df_daily_steps['ActivityDate']).dt.date

# Merging the two dataframes on Id and Date
df_METs_steps = pd.merge(df_daily_METs, df_daily_steps, left_on=['Id', 'Date'], right_on=['Id', 'ActivityDate'])

# Plotting the relationship between daily MET values and daily steps
plt.figure(figsize=(12, 6))
sns.scatterplot(x='METs', y='TotalSteps', data=df_METs_steps, alpha=0.5, color='blue')
plt.title('Relationship between Daily MET Values and Daily Steps')
plt.xlabel('Daily MET Value')
plt.ylabel('Daily Steps')
plt.show()

'''
Insights:
Positive Correlation: There appears to be a positive correlation between daily MET values and daily steps. As the MET values increase, the number of steps taken also tends to increase. This suggests that on days when users are more active (taking more steps), they also tend to have higher energy expenditure, as indicated by the MET values.

Variability in METs for Similar Step Counts: For a similar range of steps, there's a wide range of MET values. This indicates that while steps can give an indication of activity, MET values provide a more nuanced understanding of energy expenditure. Two users might take a similar number of steps, but the intensity and type of activity can result in different MET values.

Clusters of Low Activity: There's a dense cluster of data points towards the lower end of both MET values and steps. This suggests that there are many instances where users have low activity levels, both in terms of steps taken and energy expended.

Implications for Bellabeat:
Personalized Recommendations: Understanding the relationship between steps and MET values can help Bellabeat provide more personalized activity recommendations. For instance, if a user has a high step count but low MET values, it might indicate that they are walking a lot but not engaging in more intense activities. Bellabeat could then recommend activities that help increase their MET values.

Holistic View of Activity: While steps provide a straightforward measure of activity, MET values offer a more comprehensive view of a user's energy expenditure. Bellabeat can emphasize this in their marketing and product features, highlighting the importance of understanding not just how much you move, but how intensely you're moving.

Goal Setting: Users can be encouraged to set dual goals – both in terms of steps and MET values. This can help them achieve a balanced fitness routine that incorporates both general activity (steps) and more intense workouts (higher METs).
'''


-------------------------------------------------------------------



#explore the relationship between MET values and sleep patterns. Sleep is a crucial aspect of overall health, and understanding how activity levels (as indicated by MET values) correlate with sleep can provide valuable insights.


'''
To do this, we'll:

Aggregate the MET values on a daily basis for each user.
Aggregate the sleep data on a daily basis for each user, focusing on metrics like total sleep time and sleep efficiency.
Plot scatter plots to visualize the relationship between daily MET values and sleep metrics.
'''


df_sleep_day = pd.read_csv('/.../sleepDay_merged.csv')
df_sleep_day.head()

'''
Id: User ID

SleepDay: Date of the sleep record

TotalSleepRecords: Number of sleep records for the day

TotalMinutesAsleep: Total minutes the user was asleep

TotalTimeInBed: Total time the user spent in bed

'''
# Aggregating sleep data on a daily basis for each user
df_daily_sleep = df_sleep_day.groupby(['Id', 'SleepDay'])[['TotalSleepRecords', 'TotalMinutesAsleep', 'TotalTimeInBed']].mean().reset_index()
df_daily_sleep['SleepDay'] = pd.to_datetime(df_daily_sleep['SleepDay']).dt.date

# Merging the MET values and sleep dataframes on Id and Date
df_METs_sleep = pd.merge(df_daily_METs, df_daily_sleep, left_on=['Id', 'Date'], right_on=['Id', 'SleepDay'])

# Plotting the relationship between daily MET values and total minutes asleep
plt.figure(figsize=(12, 6))
sns.scatterplot(x='METs', y='TotalMinutesAsleep', data=df_METs_sleep, alpha=0.5, color='green')
plt.title('Relationship between Daily MET Values and Total Minutes Asleep')
plt.xlabel('Daily MET Value')
plt.ylabel('Total Minutes Asleep')
plt.show()

'''
Insights:

Variability in Sleep Duration: There's a wide range of sleep durations (Total Minutes Asleep) for similar MET values. This suggests that physical activity levels (as measured by METs) don't strictly dictate sleep duration for these users.

No Clear Trend: There isn't a distinct linear relationship between MET values and sleep duration. This means that higher physical activity (as measured by METs) doesn't necessarily lead to longer or shorter sleep durations.

Data Clustering: A significant portion of the data points cluster around the lower MET values and a wide range of sleep durations. This could indicate that many users have relatively low physical activity levels but varying sleep patterns.

It's essential to note that while this analysis provides insights into the relationship between physical activity and sleep for this specific dataset, other factors not present in the data might influence sleep patterns. These could include stress levels, diet, health conditions, and more.
'''



------------------------------------------------------------------------


#Exploring the relationship between MET values and heart rate

'''
Aggregate the METs and heart rate data to a common granularity (e.g., hourly or daily).
Merge the aggregated datasets based on the common identifier (Id) and timestamp.
Visualize the relationship between MET values and heart rate.
'''

df_heartrate = pd.read_csv('/.../heartrate_seconds_merged.csv')


import datetime as dt

# Convert the 'ActivityMinute' column to datetime format
df_minute_METs['ActivityMinute'] = pd.to_datetime(df_minute_METs['ActivityMinute'])

# Extract the date from 'ActivityMinute' and create a new column 'Date'
df_minute_METs['Date'] = df_minute_METs['ActivityMinute'].dt.date

# Aggregate METs data to daily granularity
daily_METs = df_minute_METs.groupby(['Id', 'Date'])['METs'].mean().reset_index()

# Convert the 'Time' column of df_heartrate to datetime format
df_heartrate['Time'] = pd.to_datetime(df_heartrate['Time'])

# Extract the date from 'Time' and create a new column 'Date'
df_heartrate['Date'] = df_heartrate['Time'].dt.date

# Aggregate heart rate data to daily granularity
daily_heartrate = df_heartrate.groupby(['Id', 'Date'])['Value'].mean().reset_index()

# Display the first few rows of the aggregated datasets
daily_METs.head(), daily_heartrate.head()


# Merge the datasets on 'Id' and 'Date'
merged_data = pd.merge(daily_METs, daily_heartrate, on=['Id', 'Date'], how='inner')

'''
METs (Metabolic Equivalent of Task): METs give an indication of the intensity of physical activity. A higher MET value indicates more intense activity. By analyzing the daily average METs, we can understand the intensity of physical activities users are engaging in on a daily basis.

Heart Rate: The heart rate data provides insights into the cardiovascular response to physical activity. A higher heart rate typically indicates more intense physical activity or stress on the cardiovascular system.

Relationship between METs and Heart Rate: By analyzing the relationship between METs and heart rate, we can infer how the intensity of physical activity (as indicated by METs) affects the heart rate. A positive correlation would suggest that as physical activity intensity increases, the heart rate also increases.

Based on these insights, Bellabeat can tailor its marketing strategies to emphasize the importance of monitoring both physical activity intensity and heart rate to achieve optimal health benefits. For instance, Bellabeat can highlight the features of its products that allow users to track both METs and heart rate, emphasizing the benefits of understanding the relationship between the two for a holistic health approach.
'''

# Plotting the relationship between daily average MET values and daily average heart rate values
plt.figure(figsize=(12, 6))
sns.scatterplot(data=merged_data, x='METs', y='Value', alpha=0.5)
plt.title('Relationship between Daily Average METs and Heart Rate')
plt.xlabel('Daily Average METs')
plt.ylabel('Daily Average Heart Rate (bpm)')
plt.grid(True)
plt.show()


# Attempting to visualize the relationship again
plt.figure(figsize=(12, 6))
sns.scatterplot(data=merged_data, x='METs', y='Value', alpha=0.5)
plt.title('Relationship between Daily Average METs and Heart Rate')
plt.xlabel('Daily Average METs')
plt.ylabel('Daily Average Heart Rate (bpm)')
plt.grid(True)
plt.tight_layout()
plt.show()
