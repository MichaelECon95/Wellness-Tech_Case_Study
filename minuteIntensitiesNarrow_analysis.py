import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

# Load the minuteIntensitiesNarrow_merged.csv data
df_minute_intensities = pd.read_csv('/.../minuteIntensitiesNarrow_merged.csv')

# Display the first few rows of the dataframe
df_minute_intensities.head()

'''
This dataset provides insights into the minute-by-minute activity intensity of users. It can help us understand the intensity and duration of physical activities users engage in.
'''

# General exploration of the minute-by-minute intensity data
# Basic information
info_minute_intensities = df_minute_intensities.info()

# Descriptive statistics
desc_stats_minute_intensities = df_minute_intensities.describe()

# Checking for missing values
missing_values_minute_intensities = df_minute_intensities.isnull().sum()

info_minute_intensities, desc_stats_minute_intensities, missing_values_minute_intensities

'''
Basic Information:
The dataset contains 1,325,580 entries.
There are 3 columns in the dataset.
No missing values are present in any of the columns.

Descriptive Statistics:

Id: User IDs range from approximately 1.50 billion to 8.88 billion.

Intensity: The average intensity value is around 0.20. The minimum is 0 (indicating no activity), and the maximum is 3. This suggests that the intensity is categorized into different levels, with 0 being the lowest and 3 being the highest.

Missing Values:
There are no missing values in the dataset.
'''

# Plotting the distribution of minute-by-minute activity intensities
plt.figure(figsize=(10, 6))
sns.countplot(x='Intensity', data=df_minute_intensities, palette='viridis')
plt.title('Distribution of Minute-by-Minute Activity Intensities')
plt.xlabel('Intensity Level')
plt.ylabel('Frequency')
plt.show()

'''
Predominance of Low Intensity: A significant majority of the data points fall under the "0" intensity level, indicating that users often have periods of minimal or no activity during many minutes of the day.

Moderate and High Intensity: There are fewer instances of intensity levels "1" and "2", suggesting that moderate and high-intensity activities are less frequent. Intensity level "3" is the least frequent, indicating that very high-intensity activities are rare.

General Trend: Most users exhibit low-intensity activities for a significant portion of the day, with occasional spikes in activity.

Understanding the activity intensity patterns can help Bellabeat in several ways:

Intensity Tracking: By understanding the intensity levels, Bellabeat can develop features that track and reward consistent moderate to high-intensity activities, motivating users to engage in more vigorous exercises.

Personalized Recommendations: The Bellabeat app can provide activity suggestions based on a user's typical intensity patterns. For example, if a user often exhibits low-intensity activities, the app might suggest short high-intensity workouts to boost metabolism and calorie burn.
'''
