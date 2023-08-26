import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns


# Load the hourlySteps_merged.csv data
df_hourly_steps = pd.read_csv('/Users/michaelcontreras/Desktop/Fitabase Data 4.12.16-5.12.16/hourlySteps_merged.csv')

# Display the first few rows of the dataframe
df_hourly_steps.head()

'''
This dataset provides insights into the hourly step count of users. It can help us understand the walking and movement patterns of users throughout the day.
'''

# General exploration of the hourly steps data
# Basic information
info_hourly_steps = df_hourly_steps.info()

# Descriptive statistics
desc_stats_hourly_steps = df_hourly_steps.describe()

# Checking for missing values
missing_values_hourly_steps = df_hourly_steps.isnull().sum()

info_hourly_steps, desc_stats_hourly_steps, missing_values_hourly_steps


'''
Basic Information:
The dataset contains 22,099 entries.
There are 3 columns in the dataset.
No missing values are present in any of the columns.

Descriptive Statistics:

Id: User IDs range from approximately 1.50 billion to 8.88 billion.

StepTotal: The average number of steps taken in an hour is around 320. The minimum is 0 (indicating no movement), and the maximum is 10,554 steps in an hour.

Missing Values:
There are no missing values in the dataset.

'''
# Plotting the distribution of hourly step counts
plt.figure(figsize=(10, 6))
sns.histplot(df_hourly_steps['StepTotal'], bins=50, kde=True)
plt.title('Distribution of Hourly Step Counts')
plt.xlabel('Number of Steps')
plt.ylabel('Frequency')
plt.show()

'''
Predominantly Low Step Counts: A significant portion of the data is clustered around lower step counts, indicating that users often have periods of minimal movement or are at rest during many hours of the day.

Few High Step Count Instances: There are fewer instances of higher step counts, suggesting that periods of continuous walking or movement are less frequent.

General Trend: Most users have a step count close to 0 for a significant portion of the day, with occasional spikes in activity.

Understanding the step count patterns can help Bellabeat in several ways:

Activity Tracking: By understanding when users are most active, Bellabeat can develop features that track and reward consistent walking or movement patterns, motivating users to maintain or increase their step counts.

Personalized Recommendations: The Bellabeat app can provide walking or movement suggestions based on a user's typical step count patterns. For example, if a user often has low step counts during the afternoon, the app might suggest a short walk to boost energy levels and meet daily step goals.
'''
