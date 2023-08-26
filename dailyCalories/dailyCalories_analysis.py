import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns


# Load the dailyCalories_merged.csv data
df_daily_calories = pd.read_csv('/Users/michaelcontreras/Desktop/Fitabase Data 4.12.16-5.12.16/dailyCalories_merged.csv')

# Display the first few rows of the dataframe
df_daily_calories.head()

# General exploration of the dailyCalories data
# Basic information
info = df_daily_calories.info()

# Descriptive statistics
desc_stats = df_daily_calories.describe()

# Checking for missing values
missing_values = df_daily_calories.isnull().sum()

info, desc_stats, missing_values

'''
General Information:

The dataset contains 940 entries.

There are three columns: Id, ActivityDay, and Calories.

Data types include integers (Id and Calories) and an object (ActivityDay).

Descriptive Statistics:

Id:
Count: 940
Mean: 4.855407e+09
Standard Deviation: 2.424805e+09
Min: 1.503960e+09
Max: 8.877689e+09

Calories:
Count: 940
Mean: 2303.61
Standard Deviation: 718.17
Min: 0
Max: 4900
Missing Values:

There are no missing values in the dataset.
The dataset provides a comprehensive view of the calories burned by users on specific days. The average calories burned per day is around 2303, with a minimum of 0 and a maximum of 4900.
'''


# Visualization of the distribution of calories burned
plt.figure(figsize=(12, 6))
sns.histplot(df_daily_calories['Calories'], bins=30, color='mediumseagreen', kde=True)
plt.title('Distribution of Calories Burned')
plt.xlabel('Calories Burned')
plt.ylabel('Frequency')
plt.grid(True)
plt.show()


'''
The distribution appears to be slightly right-skewed.
Most users burn between 1800 to 2800 calories per day.
There are some users who burn exceptionally high or low amounts of calories, as indicated by the tails of the distribution.
'''