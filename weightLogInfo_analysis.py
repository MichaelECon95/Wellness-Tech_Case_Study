import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns


# Load the weightLogInfo_merged data
df_weight_log = pd.read_csv('/.../weightLogInfo_merged.csv')

# Display the first few rows of the dataframe
df_weight_log.head()

'''
Id: User ID.
Date: The date and time of the weight log.
WeightKg: Weight of the user in kilograms.
WeightPounds: Weight of the user in pounds.
Fat: Fat percentage.
BMI: Body Mass Index.
IsManualReport: Indicates whether the weight was manually reported by the user.
LogId: Log ID.
'''

# Basic information
df_weight_log.info()

'''
The dataset contains 67 entries (rows) and 8 columns.

The columns and their non-null counts are as follows:
Id: 67 non-null values (int64)
Date: 67 non-null values (object)
WeightKg: 67 non-null values (float64)
WeightPounds: 67 non-null values (float64)
Fat: 2 non-null values (float64)
BMI: 67 non-null values (float64)
IsManualReport: 67 non-null values (bool)
LogId: 67 non-null values (int64)

The column Fat has a significant number of missing values (only 2 non-null values out of 67).

The dataset consumes approximately 3.9+ KB of memory.
'''

# Descriptive statistics
df_weight_log.describe()

'''
WeightKg:

The average weight of users in kilograms is approximately 72.04 kg.
The weight ranges from a minimum of 52.6 kg to a maximum of 133.5 kg.
50% of users have a weight less than or equal to 62.5 kg.

WeightPounds:

The average weight of users in pounds is approximately 158.81 lbs.
The weight ranges from a minimum of 115.96 lbs to a maximum of 294.32 lbs.

Fat:

The average fat percentage is 23.5%. However, it's important to note that this column has a significant number of missing values, and this average is based on only 2 non-null values.
The fat percentage ranges from 22% to 25%.

BMI:

The average BMI of users is approximately 25.19.
The BMI ranges from a minimum of 21.45 to a maximum of 47.54.
50% of users have a BMI less than or equal to 24.39.

LogId:

This column represents the unique log IDs for the weight entries.
'''

# Checking for missing values
missing_values = df_weight_log.isnull().sum()
missing_values

'''
The column Fat has 65 missing values out of 67 entries, which means that only 2 entries have non-missing values for this column.

All other columns have no missing values.
'''

# Visualization: Distribution of Weight in Kilograms
plt.figure(figsize=(10, 6))
sns.histplot(df_weight_log['WeightKg'], bins=20, kde=True, color='skyblue')
plt.title('Distribution of Weight in Kilograms')
plt.xlabel('Weight (Kg)')
plt.ylabel('Frequency')
plt.grid(axis='y')
plt.show()


'''
Visualization Type: Histogram with Kernel Density Estimation (KDE)

Why this Visualization:
A histogram is used to represent the distribution of a continuous variable, in this case, the weight of users in kilograms. The KDE line provides a smooth curve that estimates the probability density function of the variable, giving a clearer picture of the distribution shape.

Insights:

The majority of users have a weight ranging between 50 kg and 70 kg.
There's a smaller peak around the 130 kg mark, indicating a few users with higher weights.
The distribution is slightly right-skewed, meaning there are a few users with weights on the higher end, but they are less frequent compared to users with average weights.
'''


