import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

# Load the hourlyIntensities_merged.csv data
df_hourly_intensities = pd.read_csv('/.../hourlyIntensities_merged.csv')

# Display the first few rows of the dataframe
df_hourly_intensities.head()

'''
This dataset provides insights into the hourly activity intensity of users. Intensity here can be understood as the vigor or forcefulness of physical activity. Higher intensity values would indicate more vigorous activity, while lower values would indicate less active or resting periods.
'''

# General exploration of the hourly intensities data

# Basic information
info_hourly_intensities = df_hourly_intensities.info()

# Descriptive statistics
desc_stats_hourly_intensities = df_hourly_intensities.describe()

# Checking for missing values
missing_values_hourly_intensities = df_hourly_intensities.isnull().sum()

info_hourly_intensities, desc_stats_hourly_intensities, missing_values_hourly_intensities


'''
Basic Information:
The dataset contains 22,099 entries.
There are 4 columns in the dataset.
No missing values are present in any of the columns.

Descriptive Statistics:

Id: User IDs range from approximately 1.50 billion to 8.88 billion.

TotalIntensity: The average total intensity value for an hour is around 12.04, with a minimum of 0 and a maximum of 180.

AverageIntensity: The average intensity value for an hour is approximately 0.20, with a minimum of 0 and a maximum of 3.

Missing Values:
There are no missing values in the dataset.
'''

# Plotting the distribution of hourly intensities
plt.figure(figsize=(10, 6))
sns.histplot(df_hourly_intensities['AverageIntensity'], bins=50, kde=True)
plt.title('Distribution of Average Hourly Intensities')
plt.xlabel('Average Intensity per Hour')
plt.ylabel('Frequency')
plt.show()

'''
Predominantly Low Intensity: A significant portion of the data is clustered around the lower intensity values, indicating that users often engage in low-intensity activities or are at rest.

Few High Intensity Instances: There are fewer instances of higher intensity values, suggesting that periods of vigorous activity are less frequent.

General Trend: Most users have an average intensity value close to 0 for a significant portion of the day, with occasional spikes in intensity.

This data aligns with our previous findings from the calories burned dataset. Periods of higher intensity would correspond to higher caloric burns, while periods of low intensity would result in lower caloric burns.

Understanding the intensity of activities can help Bellabeat in several ways:

Personalized Recommendations: The Bellabeat app can provide activity suggestions based on a user's typical intensity patterns. For example, if a user often has low-intensity periods during the afternoon, the app might suggest a short, brisk walk to boost energy levels.
Activity Tracking: By understanding when users are most active, Bellabeat can develop features that track and reward consistent high-intensity activities, motivating users to maintain or increase their activity levels.
'''
