import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

# Load the dailyIntensities_merged.csv data
df_daily_intensities = pd.read_csv('/Users/michaelcontreras/Desktop/Fitabase Data 4.12.16-5.12.16/dailyIntensities_merged.csv')

# Display the first few rows of the dataframe
df_daily_intensities.head()


# General exploration of the dailyIntensities data

# Basic information
info_intensities = df_daily_intensities.info()

# Descriptive statistics
desc_stats_intensities = df_daily_intensities.describe()

# Checking for missing values
missing_values_intensities = df_daily_intensities.isnull().sum()

info_intensities, desc_stats_intensities, missing_values_intensities


'''
This dataset provides insights into the intensity of users' daily activities, breaking them down into categories such as sedentary, lightly active, fairly active, and very active. It also provides the distance covered in each of these categories.

Basic Information:

The dataset contains 940 entries.

There are 10 columns in the dataset.

No missing values are present in any of the columns.

Descriptive Statistics:

Id: User IDs range from approximately 1.5 billion to 8.9 billion.

SedentaryMinutes: On average, users are sedentary for about 991 minutes (or roughly 16.5 hours) per day. The maximum sedentary time recorded is 1440 minutes (or 24 hours), which indicates a full day of inactivity.

LightlyActiveMinutes: Users are lightly active for an average of about 193 minutes (or roughly 3.2 hours) per day.

FairlyActiveMinutes: Users are fairly active for an average of about 13.5 minutes per day.

VeryActiveMinutes: Users are very active for an average of about 21 minutes per day.

Distances: The distances covered in each activity intensity category are relatively small, with the most distance covered in the "LightActiveDistance" category, averaging about 3.34 units (likely kilometers or miles).

Missing Values:
There are no missing values in the dataset.
'''


# Set the style for seaborn plots
sns.set_style('whitegrid')

# Plotting the distribution of various activity intensities
activity_columns = ['SedentaryMinutes', 'LightlyActiveMinutes', 'FairlyActiveMinutes', 'VeryActiveMinutes']
plt.figure(figsize=(15, 10))

for i, column in enumerate(activity_columns, 1):
    plt.subplot(2, 2, i)
    sns.histplot(df_daily_intensities[column], bins=30, kde=True)
    plt.title(f'Distribution of {column}')
    plt.xlabel(column)
    plt.ylabel('Frequency')

plt.tight_layout()
plt.show()

'''
SedentaryMinutes: Most users have high sedentary minutes, with a peak around 1000 minutes (or roughly 16.5 hours). This indicates that a significant portion of users are inactive for a large part of the day.

LightlyActiveMinutes: The distribution shows that most users are lightly active for around 200 minutes (or roughly 3.3 hours) per day, with some variation.

FairlyActiveMinutes: Most users have fairly active minutes close to zero, with a few users reaching up to 40 minutes of fairly active time.

VeryActiveMinutes: Similar to the fairly active minutes, most users have very active minutes close to zero, with a few users reaching up to 60 minutes of very active time.

From these distributions, we can infer that a majority of users are sedentary for a significant portion of the day, with light activity being the next most common activity intensity. Fairly active and very active intensities are less common among the users.
'''

# Correlation between activity intensities and distances covered
correlation_columns = ['SedentaryMinutes', 'LightlyActiveMinutes', 'FairlyActiveMinutes', 'VeryActiveMinutes',
                       'SedentaryActiveDistance', 'LightActiveDistance', 'ModeratelyActiveDistance', 'VeryActiveDistance']
correlation_matrix = df_daily_intensities[correlation_columns].corr()

# Plotting the correlation heatmap
plt.figure(figsize=(12, 8))
sns.heatmap(correlation_matrix, annot=True, cmap='coolwarm', vmin=-1, vmax=1)
plt.title('Correlation Heatmap between Activity Intensities and Distances Covered')
plt.show()

'''
SedentaryMinutes has a very weak negative correlation with other activity intensities and distances, which is expected. As sedentary minutes increase, the time for other activities decreases.

LightlyActiveMinutes has a strong positive correlation with LightActiveDistance, indicating that as the minutes of light activity increase, the distance covered in this category also increases.

FairlyActiveMinutes and VeryActiveMinutes also show a positive correlation with their respective distances (ModeratelyActiveDistance and VeryActiveDistance).

There's a noticeable positive correlation between LightlyActiveMinutes and VeryActiveMinutes, suggesting that users who are lightly active also tend to have periods of very active behavior.

This heatmap provides insights into how different activity intensities relate to the distances covered in those categories. It also suggests patterns in user behavior, such as the relationship between light and very active minutes.
'''