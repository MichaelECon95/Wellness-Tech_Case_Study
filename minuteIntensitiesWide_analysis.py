import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

# Load the minuteIntensitiesWide_merged.csv data
df_minuteIntensitiesWide = pd.read_csv('/.../minuteIntensitiesWide_merged.csv')

# Display the first few rows of the dataframe
df_minuteIntensitiesWide.head()

'''
Id: The unique identifier for each user.
ActivityHour: The specific hour for which the activity intensity is recorded.
Intensity00 - Intensity59: These columns represent the intensity of activity for each minute within the specified hour. The values indicate the level of intensity, with higher values representing higher intensities.

Summary of the data:
This dataset provides minute-by-minute intensity levels for users throughout various hours. It can be used to understand the distribution of activity intensities throughout the day and identify patterns or trends in user behavior.
'''

# General exploration of the minute intensities data
# Basic information
df_minuteIntensitiesWide.info()

'''
21645 entries (rows)
62 columns
Each row represents the intensity of activity for a user during a specific hour. The columns Intensity00 to Intensity59 represent the intensity for each minute within that hour.

The data type for the ActivityHour column is an object (likely a string representation of the date and time), while the Id and intensity columns are integers.

There are no missing values in this dataset, which is great as it means we won't need to perform any imputation or data cleaning in that regard.
'''


# Descriptive statistics for the minute intensities data
df_minuteIntensitiesWide.describe()

'''
Intensity Values: The intensity values range from 0 to 3. The majority of the values are 0, which indicates that for most of the time, users are not engaged in any intense activity. This is evident from the 25th, 50th (median), and 75th percentiles all being 0.

Variation: The standard deviation is around 0.5 for most of the minute columns, suggesting that there isn't a significant variation in the intensity values. This further supports the observation that most of the values are 0.

Maximum Intensity: The maximum intensity value recorded is 3. This indicates that there are moments when users engage in high-intensity activities, but these moments are relatively rare compared to the low-intensity or inactive moments.

Given this information, it's evident that users have sporadic moments of high-intensity activities throughout the day, but a significant portion of their time is spent in low-intensity or inactive states.
'''

# Visualizing the distribution of intensity values for a sample hour (Intensity00 - representing the first minute of the hour)
plt.figure(figsize=(10, 6))
sns.histplot(df_minuteIntensitiesWide['Intensity00'], kde=True, bins=4)
plt.title('Distribution of Activity Intensity for the First Minute of the Hour')
plt.xlabel('Intensity Value')
plt.ylabel('Frequency')
plt.show()


'''
The histogram represents the frequency of different intensity values for the first minute of the hour.

The x-axis represents the intensity values (ranging from 0 to 3), and the y-axis represents the frequency of occurrences.

A significant majority of the data points have an intensity value of 0, indicating that most users are inactive or engage in very low-intensity activities during the first minute of any given hour.

There are fewer occurrences of intensity values 1 and 2, suggesting moments of moderate activity.

Very few data points have an intensity value of 3, indicating that high-intensity activities during the first minute of the hour are rare.

This visualization provides a snapshot of user activity patterns for just one minute of the hour. To get a comprehensive understanding, similar patterns can be observed across all minutes. 
However, this sample gives us an idea that a significant portion of users' time is spent in a state of low activity or inactivity.

'''
