import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

# Load the hourlyCalories_merged.csv data
df_hourly_calories = pd.read_csv('/Users/michaelcontreras/Desktop/Fitabase Data 4.12.16-5.12.16/hourlyCalories_merged.csv')

# Display the first few rows of the dataframe
df_hourly_calories.head()

'''
This dataset provides insights into the hourly calorie burn of users. It can help us understand the activity levels and energy expenditure patterns of users throughout the day.
'''

# General exploration of the hourly calories data
# Basic information
info_hourly_calories = df_hourly_calories.info()

# Descriptive statistics
desc_stats_hourly_calories = df_hourly_calories.describe()

# Checking for missing values
missing_values_hourly_calories = df_hourly_calories.isnull().sum()

info_hourly_calories, desc_stats_hourly_calories, missing_values_hourly_calories


'''
Basic Information:
The dataset contains 22,099 entries.
There are 3 columns in the dataset.
No missing values are present in any of the columns.

Descriptive Statistics:

Id: User IDs range from approximately 1.50 billion to 8.88 billion.

Calories: On average, users burn about 97.39 calories per hour. The minimum number of calories burned in an hour is 42, and the maximum is a significant 948. The 25th percentile is at 63 calories, the median (50th percentile) is at 83 calories, and the 75th percentile is at 108 calories.

Missing Values:
There are no missing values in the dataset.
'''

# Plotting the distribution of hourly calories burned
plt.figure(figsize=(10, 6))
sns.histplot(df_hourly_calories['Calories'], bins=50, kde=True)
plt.title('Distribution of Hourly Calories Burned')
plt.xlabel('Calories Burned per Hour')
plt.ylabel('Frequency')
plt.show()


'''
Peak at Low Caloric Burn: There's a pronounced peak around 60-80 calories burned per hour. This suggests that for a significant portion of the day, users are engaged in low-intensity activities or are at rest.

Few High Caloric Burns: There are fewer instances where users burn a high number of calories in an hour. These instances likely correspond to periods of intense physical activity or exercise.

General Trend: Most users burn between 40 and 150 calories per hour, with fewer occurrences outside this range.

This data provides valuable insights into the activity levels of users. For a company like Bellabeat, understanding when users are most active (burning the most calories) can help in tailoring product features or marketing strategies. For instance, if a user tends to burn more calories during a particular time of day, the Bellabeat app could provide timely reminders or motivational messages during those hours.
'''