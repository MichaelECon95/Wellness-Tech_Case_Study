import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns



# Load the minuteCaloriesNarrow_merged.csv data
df_minute_calories = pd.read_csv('/Users/michaelcontreras/Desktop/Fitabase Data 4.12.16-5.12.16/minuteCaloriesNarrow_merged.csv')

# Display the first few rows of the dataframe
df_minute_calories.head()

'''
This dataset provides insights into the minute-by-minute calorie burn rate of users. It can help us understand the intensity and duration of physical activities users engage in.
'''
# General exploration of the minute-by-minute calorie data
# Basic information
info_minute_calories = df_minute_calories.info()

# Descriptive statistics
desc_stats_minute_calories = df_minute_calories.describe()

# Checking for missing values
missing_values_minute_calories = df_minute_calories.isnull().sum()

info_minute_calories, desc_stats_minute_calories, missing_values_minute_calories


'''
Basic Information:
The dataset contains 1,325,580 entries.
There are 3 columns in the dataset.
No missing values are present in any of the columns.

Descriptive Statistics:

Id: User IDs range from approximately 1.50 billion to 8.88 billion.

Calories: The average number of calories burned per minute is around 1.62. The minimum is 0 (indicating no activity), and the maximum is approximately 19.75 calories burned in a minute.

Missing Values:

There are no missing values in the dataset.
'''

# Plotting the distribution of minute-by-minute calorie burn rates
plt.figure(figsize=(10, 6))
sns.histplot(df_minute_calories['Calories'], bins=50, kde=True)
plt.title('Distribution of Minute-by-Minute Calorie Burn Rates')
plt.xlabel('Calories Burned per Minute')
plt.ylabel('Frequency')
plt.show()

'''
Low Calorie Burn Predominance: A significant portion of the data is clustered around lower calorie burn rates, indicating that users often have periods of minimal activity or are at rest during many minutes of the day.

Few High Calorie Burn Instances: There are fewer instances of higher calorie burn rates, suggesting that periods of intense physical activity are less frequent.

General Trend: Most users burn a minimal number of calories for a significant portion of the day, with occasional spikes in activity.

Understanding the calorie burn patterns can help Bellabeat in several ways:

Activity Intensity Tracking: By understanding when users are burning more calories, Bellabeat can develop features that track and reward consistent high-intensity activities, motivating users to engage in more vigorous exercises.
Personalized Recommendations: The Bellabeat app can provide activity suggestions based on a user's typical calorie burn patterns. For example, if a user often burns minimal calories during the afternoon, the app might suggest a short high-intensity workout to boost metabolism and calorie burn.
'''
