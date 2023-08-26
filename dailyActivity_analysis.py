import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

# Load the first data file
data_file_path = '/.../dailyActivity_merged.csv'
df_daily_activity = pd.read_csv(data_file_path)

# Display the first few rows of the dataset
df_daily_activity.head()


'''
Id: Identifier for the user.

ActivityDate: Date of the activity.

TotalSteps: Total number of steps taken on that day.

TotalDistance: Total distance covered on that day.

TrackerDistance: Distance tracked by the device.

LoggedActivitiesDistance: Distance from logged activities.

VeryActiveDistance: Distance covered during very active periods.

ModeratelyActiveDistance: Distance covered during moderately active periods.

LightActiveDistance: Distance covered during light activity.

SedentaryActiveDistance: Distance covered during sedentary periods.

VeryActiveMinutes: Minutes of very active activity.

FairlyActiveMinutes: Minutes of fairly active activity.

LightlyActiveMinutes: Minutes of light activity.

SedentaryMinutes: Sedentary minutes.

Calories: Calories burned.
'''
# Check for missing values
missing_values = df_daily_activity.isnull().sum()

# Get summary statistics for the numerical columns
summary_statistics = df_daily_activity.describe()

missing_values, summary_statistics

'''
Missing Values:
There are no missing values in the dailyActivity_merged.csv dataset. Every column is complete.

Summary Statistics:

TotalSteps: Users take an average of around 7,638 steps per day, with a maximum of 36,019 steps and a minimum of 0 steps.

TotalDistance: The average distance covered is approximately 5.49 km, with a maximum of 28.03 km and a minimum of 0 km.

Calories: On average, users burn around 2,303 calories per day, with a maximum of 4,900 calories and a minimum of 0 calories.

VeryActiveMinutes: Users spend an average of 21 minutes in very active activities, with a maximum of 210 minutes.

SedentaryMinutes: Users spend an average of 991 minutes being sedentary, with a maximum of 1,440 minutes (which is equivalent to 24 hours).

'''


fig, axes = plt.subplots(nrows=3, ncols=1, figsize=(12, 15))

# Plot distribution of TotalSteps
sns.histplot(df_daily_activity['TotalSteps'], kde=True, ax=axes[0], color='skyblue')
axes[0].set_title('Distribution of Total Steps')
axes[0].set_xlabel('Total Steps')
axes[0].set_ylabel('Frequency')

# Plot distribution of TotalDistance
sns.histplot(df_daily_activity['TotalDistance'], kde=True, ax=axes[1], color='salmon')
axes[1].set_title('Distribution of Total Distance (km)')
axes[1].set_xlabel('Total Distance (km)')
axes[1].set_ylabel('Frequency')

# Plot distribution of Calories
sns.histplot(df_daily_activity['Calories'], kde=True, ax=axes[2], color='lightgreen')
axes[2].set_title('Distribution of Calories Burned')
axes[2].set_xlabel('Calories Burned')
axes[2].set_ylabel('Frequency')

plt.tight_layout()
plt.show()

'''
Distribution of Total Steps:

Most users take between 0 to 10,000 steps daily, with a peak around 5,000 steps.
There are some users who take more than 20,000 steps, but they are relatively fewer.
Distribution of Total Distance (km):

The majority of users cover a distance between 0 to 10 km daily, with a peak around 2.5 km.
Few users cover distances greater than 20 km.
Distribution of Calories Burned:

The calorie burn distribution is slightly right-skewed, with most users burning between 1500 to 3000 calories daily.
There's a small peak around 0, indicating some users who didn't burn any calories (possibly they didn't wear the device or were inactive).
These visualizations give us an initial understanding of the general activity levels of the users in the dataset.

'''


#Deeper analysis
'''
Activity Levels: 
I'll categorize users based on their daily step count to understand the proportion of users in each activity level (e.g., Sedentary, Lightly Active, Active, Highly Active).

Active vs. Sedentary Minutes: We'll analyze the distribution of active minutes (sum of VeryActiveMinutes, FairlyActiveMinutes, and LightlyActiveMinutes) compared to SedentaryMinutes.

Calories Burned vs. Activity: We'll explore how calorie burn relates to the total steps taken.
'''

# Categorize users based on their daily step count
bins = [0, 2500, 5000, 10000, 40000]
labels = ['Sedentary', 'Lightly Active', 'Active', 'Highly Active']
df_daily_activity['Activity Level'] = pd.cut(df_daily_activity['TotalSteps'], bins=bins, labels=labels, right=False)

# Plot the distribution of activity levels
activity_level_counts = df_daily_activity['Activity Level'].value_counts(normalize=True) * 100
activity_level_counts.sort_index().plot(kind='bar', color='mediumpurple', figsize=(10, 6))
plt.title('Distribution of Activity Levels based on Daily Step Count')
plt.xlabel('Activity Level')
plt.ylabel('Percentage of Users (%)')
plt.xticks(rotation=45)
plt.grid(axis='y')
plt.show()

'''
Sedentary: Users taking less than 2,500 steps. This group represents around 20% of the users.

Lightly Active: Users taking between 2,500 to 5,000 steps. This is the largest group, comprising around 35% of the users.

Active: Users taking between 5,000 to 10,000 steps. This group represents around 30% of the users.

Highly Active: Users taking more than 10,000 steps. This group represents around 15% of the users.

From this, we can infer that a significant portion of users (around 55%) are either sedentary or lightly active, while the remaining 45% are more active.
'''



# Calculate total active minutes and compare with sedentary minutes
df_daily_activity['TotalActiveMinutes'] = df_daily_activity['VeryActiveMinutes'] + df_daily_activity['FairlyActiveMinutes'] + df_daily_activity['LightlyActiveMinutes']

fig, ax = plt.subplots(figsize=(12, 6))
sns.kdeplot(df_daily_activity['TotalActiveMinutes'], shade=True, label='Total Active Minutes', ax=ax, color='royalblue')
sns.kdeplot(df_daily_activity['SedentaryMinutes'], shade=True, label='Sedentary Minutes', ax=ax, color='tomato')
ax.set_title('Distribution of Active vs. Sedentary Minutes')
ax.set_xlabel('Minutes')
ax.set_ylabel('Density')
plt.legend()
plt.grid(axis='y')
plt.show()



'''
Total Active Minutes: This represents the sum of VeryActiveMinutes, FairlyActiveMinutes, and LightlyActiveMinutes. The distribution shows that most users have active minutes ranging from 0 to around 300 minutes daily, with a peak around 50 minutes.

Sedentary Minutes: This represents the time users are inactive. The distribution is right-skewed, indicating that a significant number of users have high sedentary minutes, with a peak around 600 minutes (or 10 hours).

From this visualization, we can infer that while users do engage in active behaviors, they also spend a significant portion of their day being sedentary.
'''


# Scatter plot to visualize the relationship between TotalSteps and Calories burned
plt.figure(figsize=(12, 6))
sns.scatterplot(x=df_daily_activity['TotalSteps'], y=df_daily_activity['Calories'], alpha=0.6, color='seagreen')
plt.title('Relationship between Total Steps and Calories Burned')
plt.xlabel('Total Steps')
plt.ylabel('Calories Burned')
plt.grid(True)
plt.show()


'''
The scatter plot illustrates the relationship between the total number of steps taken and the calories burned:

As expected, there's a positive correlation between the number of steps taken and the calories burned. This means that as users take more steps, they tend to burn more calories.

The data points are more concentrated towards the lower end, indicating that most users take fewer steps and consequently burn fewer calories.

There are a few outliers where users have taken a significant number of steps but burned relatively fewer calories. This could be due to factors like the user's metabolic rate, the intensity of the steps (e.g., walking vs. running), or inaccuracies in the device's calorie estimation.
'''



#explore relationships between other metrics
'''
Specifically, I'll look at the relationship between VeryActiveMinutes and Calories burned to see if more intense activity results in a higher calorie burn. 

I'll also explore the relationship between SedentaryMinutes and Calories to understand the impact of inactivity on calorie burn.
'''

fig, (ax1, ax2) = plt.subplots(1, 2, figsize=(18, 6))

# Relationship between VeryActiveMinutes and Calories burned
sns.scatterplot(x=df_daily_activity['VeryActiveMinutes'], y=df_daily_activity['Calories'], alpha=0.6, color='dodgerblue', ax=ax1)
ax1.set_title('Relationship between Very Active Minutes and Calories Burned')
ax1.set_xlabel('Very Active Minutes')
ax1.set_ylabel('Calories Burned')
ax1.grid(True)

# Relationship between SedentaryMinutes and Calories burned
sns.scatterplot(x=df_daily_activity['SedentaryMinutes'], y=df_daily_activity['Calories'], alpha=0.6, color='coral', ax=ax2)
ax2.set_title('Relationship between Sedentary Minutes and Calories Burned')
ax2.set_xlabel('Sedentary Minutes')
ax2.set_ylabel('Calories Burned')
ax2.grid(True)

plt.tight_layout()
plt.show()


'''
Very Active Minutes vs. Calories Burned:

There's a positive correlation between very active minutes and calories burned. As the duration of very active minutes increases, the number of calories burned also increases.
This suggests that engaging in high-intensity activities leads to a higher calorie burn.
Sedentary Minutes vs. Calories Burned:

There's a wide spread in the data, but we can observe a general trend: as sedentary minutes increase, the range of calories burned narrows and tends to be on the lower side.
This indicates that prolonged sedentary behavior might be associated with lower calorie expenditure.


From these insights, Bellabeat can emphasize the importance of engaging in high-intensity activities to burn more calories and highlight the potential negative effects of prolonged sedentary behavior on calorie burn.
'''


#Relationship between TotalDistance covered and Calories burned. This will help us understand if longer distances covered (through walking, running, etc.) result in a higher calorie burn.

# Scatter plot to visualize the relationship between TotalDistance and Calories burned
plt.figure(figsize=(12, 6))
sns.scatterplot(x=df_daily_activity['TotalDistance'], y=df_daily_activity['Calories'], alpha=0.6, color='mediumorchid')
plt.title('Relationship between Total Distance Covered and Calories Burned')
plt.xlabel('Total Distance (in miles)')
plt.ylabel('Calories Burned')
plt.grid(True)
plt.show()

'''
The scatter plot illustrates the relationship between the total distance covered and the calories burned:

There's a clear positive correlation between the distance covered and the calories burned. As users cover more distance (through walking, running, etc.), they tend to burn more calories.

The data points are more concentrated towards the lower end, indicating that most users cover shorter distances and consequently burn fewer calories.

This insight can be valuable for Bellabeat. Encouraging users to cover more distance, even through simple activities like walking, can lead to a higher calorie burn. This can be a motivating factor for users to be more active.
'''
