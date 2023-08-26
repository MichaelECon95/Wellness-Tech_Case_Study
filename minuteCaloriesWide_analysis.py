import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns


# Load the minuteCaloriesWide_merged.csv data
df_minuteCaloriesWide = pd.read_csv('/.../minuteCaloriesWide_merged.csv')

# Display the first few rows of the dataframe
df_minuteCaloriesWide.head()

'''
The dataset provides hourly calorie burn data for different users. Each row represents an hour of a day for a specific user, and the columns represent the calories burned in each minute of that hour.

Summary of the data:
Id: The ID of the user.
ActivityHour: The specific hour for which the data is recorded.
Calories00 - Calories59: Represents the calories burned in each minute of the hour.
'''
# Basic information about the dataframe
df_minuteCaloriesWide.info()

'''
21,645 entries (rows)
62 columns
The columns represent:

Id: User ID (integer type)
ActivityHour: The specific hour for which the data is recorded (object type)
Calories00 - Calories59: Represents the calories burned in each minute of the hour (all float64 type)
There are no missing values in this dataset.

'''

# Descriptive statistics for the dataframe
df_minuteCaloriesWide.describe()

'''
Count: There are 21,645 entries for each minute.
Mean: On average, users burn around 1.62 to 1.64 calories per minute throughout the hour.
Std: The standard deviation, which measures the amount of variation or dispersion of the data, is around 1.39 to 1.44 calories per minute. This indicates that the calorie burn rate varies quite a bit from minute to minute.
Min: The minimum calories burned in a minute is 0.7027.
25%: 25% of the data points have a calorie burn rate of approximately 0.9357 per minute.
50% (Median): The median calorie burn rate is around 1.2176 to 1.2204 per minute.
75%: 75% of the data points have a calorie burn rate of up to approximately 1.4327 per minute.
Max: The maximum calories burned in a minute is 19.7273.
This provides a general idea about the distribution of calorie burn rates for each minute of the hour.

'''

# Double Checking for missing values in the dataframe
missing_values = df_minuteCaloriesWide.isnull().sum()
missing_values[missing_values > 0]


#Line Plot: Average Calorie Burn Rate for Each Minute of the Hour
#I'll use a line plot to visualize this data because it's an effective way to display continuous data over time and can help identify trends or patterns.


# Calculate the average calorie burn rate for each minute of the hour
avg_calories_per_minute = df_minuteCaloriesWide.iloc[:, 2:].mean()

# Plotting the average calorie burn rate for each minute
plt.figure(figsize=(15, 6))
sns.lineplot(x=avg_calories_per_minute.index, y=avg_calories_per_minute.values)
plt.title('Average Calorie Burn Rate for Each Minute of the Hour')
plt.xlabel('Minute')
plt.ylabel('Average Calorie Burn Rate')
plt.xticks(rotation=45)
plt.tight_layout()
plt.show()


'''
Line Plot Summary:
The line plot showcases the average calorie burn rate for each minute of the hour. Here are some observations:

The calorie burn rate remains relatively consistent throughout the hour, with minor fluctuations.

There aren't any significant spikes or drops, indicating that the calorie burn rate is steady for most users.

The average calorie burn rate hovers around 1.6 calories per minute.

This visualization provides a clear picture of how users, on average, burn calories throughout the hour. The consistency in the calorie burn rate suggests that users maintain a relatively steady level of activity during these hours.
'''



