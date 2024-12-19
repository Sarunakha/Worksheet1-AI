# -*- coding: utf-8 -*-
"""assignment1.ipynb

Automatically generated by Colab.

Original file is located at
    https://colab.research.google.com/drive/1MfLP8bBJH0m-duZyRQhZiPTNdQPaYrzV

#**Name: Saruna Khadka**

#**Student ID: 2407950**

#3.1 Problem - 1: Getting Started with Data Exploration - Some Warm up
**Exercises:**

**1. Data Exploration and Understanding:**

• Dataset Overview:

1. Load the dataset and display the first 10 rows.
2. Identify the number of rows and columns in the dataset.
3. List all the columns and their data types.

• Basic Statistics:
1. Calculate the mean, median, and standard deviation for the Score column.
2. Identify the country with the highest and lowest happiness scores.

• Missing Values:
1. Check if there are any missing values in the dataset. If so, display the total count for each column.

• Filtering and Sorting:
1. Filter the dataset to show only the countries with a Score greater than 7.5.
2. For the filtered dataset - Sort the dataset by GDP per Capita in descending order and display the
top 10 rows.

• Adding New Columns:
1. Create a new column called Happiness Category that categorizes countries into three categories
based on their Score:

Low − (Score < 4)

Medium − (4 ≤ Score ≤ 6)

High − (Score > 6)
"""

import pandas as pd
df = pd.read_csv('/content/drive/MyDrive/assignment-1/WHR-2024-5CS037.csv')
df

df.head(10)

rows, columns = df.shape
rows, columns

columns = df.columns
datatypes = df.dtypes
columns, datatypes

mean = df['score'].mean()
median = df['score'].median()
std = df['score'].std()
mean, median, std

highest_score = df[df['score'] == df['score'].max()]
lowest_score = df[df['score'] == df['score'].min()]
highest_score, lowest_score

missing_values = df.isnull().sum()
missing_values

missing_values = missing_values[missing_values > 0]
missing_values

filtered_df = df[df['score'] > 7.5]
filtered_df

sorted_df = filtered_df.sort_values(by='Log GDP per capita', ascending=False)
top_10_rows = sorted_df.head(10)
top_10_rows

import numpy as np
conditions = [
    df['score'] < 4,
    (df['score'] >= 4) & (df['score'] <= 6),
    df['score'] > 6
]
categories = ['Low', 'Medium', 'High']
df['Happiness Category'] = np.select(conditions, categories)
df[['score', 'Happiness Category']]

"""2. Data Visualizations:

• Bar Plot: Plot the top 10 happiest countries by Score using a bar chart.

• Line Plot: Plot the top 10 unhappiest countries by Score using a Line chart.

• Plot a histogram for the Score column to show its distribution and also interpret.

• Scatter Plot: Plot a scatter plot between GDP per Capita and Score to visualize their relationship.
"""

import matplotlib.pyplot as plt
import seaborn as sns
sns.set(style="whitegrid")
top_10_happiest = df.nlargest(10, 'score')
plt.figure(figsize=(12, 6))
sns.barplot(x='Country name', y='score', data=top_10_happiest)
plt.title('Top 10 Happiest Countries by Score')
plt.xlabel('Country')
plt.ylabel('Score')
plt.show()

top_10_unhappiest = df.nsmallest(10, 'score')
plt.figure(figsize=(12, 6))
sns.lineplot(x='Country name', y='score', data=top_10_unhappiest)
plt.title('Top 10 Unhappiest Countries by Score')
plt.xlabel('Country')
plt.ylabel('Score')
plt.show

plt.figure(figsize=(8, 4))
sns.histplot(df['score'], bins=20, kde=True)
plt.title('Distribution of Score')
plt.xlabel('Score')
plt.ylabel('Frequency')
plt.show()

plt.figure(figsize=(10, 6))
sns.scatterplot(x='Log GDP per capita', y='score', data=df)
plt.title('Relationship between GDP per Capita and Score')
plt.xlabel('Log GDP per Capita')
plt.ylabel('Score')

"""3.2 Problem - 2 - Some Advance Data Exploration

Task:

Task - 1 - Setup Task - Preparing the South-Asia Dataset:
Steps:
1. Define the countries in South Asia with a list for example:
south asian countries = ["Afghanistan", "Bangladesh", "Bhutan", "India",

"Maldives", "Nepal", "Pakistan", "Srilanka"]

2. Use the list from step - 1 to filtered the dataset {i.e. filtered out matching dataset from list.}
3. Save the filtered dataframe as separate CSV files for future use.
"""

south_asian_countries = ["Afghanistan", "Bangladesh", "Bhutan", "India", "Maldives", "Nepal", "Pakistan", "Sri Lanka"]
filtered_df1 = df[df['Country name'].isin(south_asian_countries)]
filtered_df1

filtered_df1.to_csv('south_asian_countries.csv', index=False)

"""Task - 2 - Composite Score Ranking:

Tasks:

1. Using the SouthAsia DataFrame, create a new column called Composite Score that combines the
following metrics:

Composite Score = 0.40 × GDP per Capita + 0.30 × Social Support

+ 0.30 × Healthy Life Expectancy
2. Rank the South Asian countries based on the Composite Score in descending order.
3. Visualize the top 5 countries using a horizontal bar chart showing the Composite Score.
4. Discuss whether the rankings based on the Composite Score align with the original Score - support your
discussion with some visualization plot.

"""

Composite_score = 0.40 * filtered_df1['Log GDP per capita'] + 0.30 * filtered_df1['Social support'] + 0.30 * filtered_df1['Healthy life expectancy']
filtered_df1['Composite Score'] = Composite_score
filtered_df1

ranked_south_asian_countries = filtered_df1.sort_values(by='Composite Score', ascending=False)
ranked_south_asian_countries

import matplotlib.pyplot as plt
import seaborn as sns
top_5_south_asia = ranked_south_asian_countries.sort_values(by='Composite Score',ascending=False).head(5)
plt.figure(figsize=(8, 4))
sns.barplot(x='Composite Score', y='Country name', data=top_5_south_asia, color='skyblue')
plt.title('Top 5 South Asian Countries by Composite Score', fontsize=16)
plt.xlabel('Composite Score', fontsize=12)
plt.ylabel('Country', fontsize=12)
plt.show()

ranked_south_asia_original = ranked_south_asian_countries.sort_values(by='score', ascending=False)
plt.figure(figsize=(10, 4))
sns.barplot(x='score', y='Country name', data=top_5_south_asia, label='Original Score', color='pink')
sns.barplot(x='Composite Score', y='Country name', data=top_5_south_asia, label='Composite Score', color='gray')
plt.title('Comparison of Composite Score and Original Score (Top 5 Countries)', fontsize=16)
plt.xlabel('score')
plt.ylabel('Country name')
plt.legend()
plt.show()

"""If the rankings based on the "Composite Score" are similar to the "score," or original score, then the factors that were utilized to create the "Composite Score"—Log GPD per capita, social support, and healthy life expectancy—are consistent with the happiness assessment.

Additionally, if the ranks are different, it means that the original "score" included other factors that the "Composite Score" did not.

In a similar vein, we can see that there is a discrepancy between the "Composite Score" and the original score.

Task - 3 - Outlier Detection:

Tasks:
1. Identify outlier countries in South Asia based on their Score and GDP per Capita.
2. Define outliers using the 1.5 × IQR rule.
3. Create a scatter plot with GDP per Capita on the x-axis and Score on the y-axis, highlighting outliers
in a different color.
4. Discuss the characteristics of these outliers and their potential impact on regional averages.
"""

Q1_score = filtered_df1['score'].quantile(0.25)
Q3_score = filtered_df1['score'].quantile(0.75)
IQR_score = Q3_score - Q1_score

Q1_gdp = filtered_df1['Log GDP per capita'].quantile(0.25)
Q3_gdp = filtered_df1['Log GDP per capita'].quantile(0.75)
IQR_gdp = Q3_gdp - Q1_gdp

lower_bound_score = Q1_score - 1.5 * IQR_score
upper_bound_score = Q3_score + 1.5 * IQR_score

lower_bound_gdp = Q1_gdp - 1.5 * IQR_gdp
upper_bound_gdp = Q3_gdp + 1.5 * IQR_gdp

outliers_score = filtered_df1[(filtered_df1['score'] < lower_bound_score) | (filtered_df1['score'] > upper_bound_score)]
outliers_gdp = filtered_df1[(filtered_df1['Log GDP per capita'] < lower_bound_gdp) | (filtered_df1['Log GDP per capita'] > upper_bound_gdp)]
outliers = pd.concat([outliers_score, outliers_gdp])
outliers

plt.figure(figsize=(10, 6))
sns.scatterplot(x='Log GDP per capita', y='score', data=filtered_df1,label='original data',color='green')
sns.scatterplot(x='Log GDP per capita', y='score', data=outliers,label='outlier',color='red')
plt.title('Outlier Detection in South Asia')
plt.xlabel('Log GDP per Capita')
plt.ylabel('Score')
plt.legend()
plt.show()

"""Outliers in Scores:
Outliers in the "Score" category indicate countries that deviate significantly from the typical regional distribution of happiness levels. These deviations may highlight unique societal or cultural factors influencing how happiness is measured and perceived in these nations.

Outliers in GDP:
Outliers in the "GDP per Capita" category represent countries with either significantly higher or lower economic performance compared to the regional average. Nations with low GDP values often indicate economically underdeveloped or impoverished regions, whereas those with high GDP values typically reflect industrialized countries with substantial wealth per individual.

Regional Impact:
The presence of outliers can distort regional averages. Countries with extremely high or low happiness scores can disproportionately influence the average happiness level of the region. Similarly, nations with exceptionally high or low GDP per capita may skew the regional economic indicators. For instance, Afghanistan, with its low GDP per capita, may reduce the overall regional GDP average.

Task - 4 - Exploring Trends Across Metrics:

Tasks:
1. Choose two metrics (e.g., Freedom to Make Life Choices and Generosity) and calculate their correlation
{pearson correlation} with the Score for South Asian countries.
2. Create scatter plots with trendlines for these metrics against the Score.
3. Identify and discuss the strongest and weakest relationships between these metrics and the Score for
South Asian countries.
"""

correlation_freedom_score = filtered_df1['Freedom to make life choices'].corr(filtered_df1['score'])
correlation_generosity_score = filtered_df1['Generosity'].corr(filtered_df1['score'])
correlation_freedom_score, correlation_generosity_score

plt.figure(figsize=(8, 4))
sns.regplot(x='Freedom to make life choices', y='score', data=filtered_df)
plt.title('Correlation between Freedom to Make Life Choices and Score')
plt.xlabel('Freedom to Make Life Choices')
plt.ylabel('Score')
plt.show()

plt.figure(figsize=(8, 4))
sns.regplot(x='Generosity', y='score', data=filtered_df)
plt.title('Correlation between Generosity and Score')
plt.xlabel('Generosity')
plt.ylabel('Score')
plt.show()

"""Task - 5 - Gap Analysis:

Tasks:

1. Add a new column, GDP-Score Gap, which is the difference between GDP per Capita and the Score
for each South Asian country.
2. Rank the South Asian countries by this gap in both ascending and descending order.
3. Highlight the top 3 countries with the largest positive and negative gaps using a bar chart.
4. Analyze the reasons behind these gaps and their implications for South Asian countries.
"""

GDP_Score_Gap = filtered_df1['Log GDP per capita'] - filtered_df1['score']
filtered_df1['GDP-Score Gap'] = GDP_Score_Gap
filtered_df1

ranked_by_gap = filtered_df1.sort_values(by='GDP-Score Gap', ascending=False)
ranked_by_gap

ranked_by_gap = filtered_df1.sort_values(by='GDP-Score Gap', ascending=True)
ranked_by_gap

ranked_by_gap_positive = ranked_by_gap.sort_values(by='GDP-Score Gap', ascending=False).head(3)
ranked_by_gap_positive

ranked_by_gap_negative = ranked_by_gap.sort_values(by='GDP-Score Gap', ascending=True).head(3)
ranked_by_gap_negative

"""3.3 Problem - 3 - Comparative Analysis:

Task - 1 - Setup Task - Preparing the Middle Eastern Dataset:

Tasks:

1. Similar in Task - 1 of Problem 2 create a dataframe from middle eastern countries. For hint use the
following list:
middle east countries = [ "Bahrain", "Iran", "Iraq", "Israel", "Jordan",
"Kuwait", "Lebanon", "Oman", "Palestine", "Qatar", "Saudi Arabia", "Syria",

"United Arab Emirates", "Yemen"]

Complete the following task:

1. Descriptive Statistics:

• Calculate the mean, Standard deviation of the score for both South Asia and Middle East.

• Which region has higher happiness Scores on average?

2. Top and Bottom Performers:

• Identify the top 3 and bottom 3 countries in each region based on the score.

• Plot bar charts comparing these charts.

3. Metric Comparisons:

• Compare key metrics like GDP per Capita, Social Support, and Healthy Life Expectancy between the regions using grouped bar charts.

• Which metrics show the largest disparity between the two regions?

4. Happiness Disparity:

• Compute the range (max - min) and coefficient of variation (CV) for Score in both regions.

• Which region has greater variability in happiness?

5. Correlation Analysis:

• Analyze the correlation of Score with other metrics Freedom to Make Life Choices, and Generosity within each region.

• Create scatter plots to visualize and interpret the relationships.

6. Outlier Detection:

• Identify outlier countries in both regions based on Score and GDP per Capita.

• Plot these outliers and discuss their implications.

7. Visualization:

• Create boxplots comparing the distribution of Score between South Asia and the Middle East.

• Interpret the key differences in distribution shapes, medians, and outliers.
"""

middle_east_countries = ["Bahrain", "Iran", "Iraq", "Israel", "Jordan", "Kuwait", "Lebanon",
                         "Oman", "Palestine", "Qatar", "Saudi Arabia", "Syria",
                         "United Arab Emirates", "Yemen"]
filtered_df2 = df[df['Country name'].isin(middle_east_countries)]
filtered_df2

mean_of_south_asia = filtered_df1['score'].mean()
std_of_south_asia = filtered_df1['score'].std()
mean_of_middle_east = filtered_df2['score'].mean()
std_of_middle_east = filtered_df2['score'].std()
mean_of_south_asia, std_of_south_asia, mean_of_middle_east, std_of_middle_east

south_asia_top3 = filtered_df1.nlargest(3, 'score')
south_asia_bottom3 = filtered_df1.nsmallest(3, 'score')
middle_east_top3 = filtered_df2.nlargest(3, 'score')
middle_east_bottom3 = filtered_df2.nsmallest(3, 'score')
south_asia_top3, south_asia_bottom3, middle_east_top3, middle_east_bottom3

plt.figure(figsize=(9,4))
sns.barplot(data=pd.concat([middle_east_top3, middle_east_bottom3]), x='Country name', y='score')
plt.title('Middle East: Top 3 and Bottom 3 Happiness Scores')
plt.show()

plt.figure(figsize=(8, 4))
sns.barplot(data=pd.concat([south_asia_top3, south_asia_bottom3]), x='Country name', y='score')
plt.title('South Asia: Top 3 and Bottom 3 Happiness Scores')
plt.show()

#comparing key metrics and caluating the mean value for each metric by region
metrics = ['Log GDP per capita', 'Social support', 'Healthy life expectancy']
regions = ['Middle East', 'South Asia']

#combining the mean values into a single dataframe
metrics_comparison = pd.DataFrame({
    'Metric': metrics,
    'Middle East': [filtered_df2[metric].mean() for metric in metrics],
    'South Asia': [filtered_df1[metric].mean() for metric in metrics]
})

#calculating absolute disparity for each metric
metrics_comparison['Disparity'] = abs(metrics_comparison['Middle East'] - metrics_comparison['South Asia'])

metrics_comparison_melted = metrics_comparison.melt(
    id_vars='Metric',
    value_vars=['Middle East', 'South Asia'],
    var_name='Region',
    value_name='Average Value'
)

#add labels and title
plt.figure(figsize=(10, 6))
sns.barplot(data=metrics_comparison_melted, x='Metric', y='Average Value', hue='Region')
plt.title('Metric Comparisons Between Regions')
plt.ylabel('Average Value')
plt.xlabel('Metric')
plt.show()

print("Disparity between Middle East and South Asia for each metric:")
print(metrics_comparison[['Metric', 'Disparity']])

#correlation for middde east based on freedom and generosity
middle_east_corr_freedom = filtered_df2['score'].corr(filtered_df2['Freedom to make life choices'])
middle_east_corr_generosity = filtered_df2['score'].corr(filtered_df2['Generosity'])

#correlation for south asian based on freedom and generosity
south_asia_corr_freedom = filtered_df1['score'].corr(filtered_df1['Freedom to make life choices'])
south_asia_corr_generosity = filtered_df1['score'].corr(filtered_df1['Generosity'])

print("Correlation Analysis:")
print(f"Middle East - Score vs Freedom to Make Life Choices: {middle_east_corr_freedom:.2f}")
print(f"Middle East - Score vs Generosity: {middle_east_corr_generosity:.2f}")
print(f"South Asia - Score vs Freedom to Make Life Choices: {south_asia_corr_freedom:.2f}")
print(f"South Asia - Score vs Generosity: {south_asia_corr_generosity:.2f}")

# Scatter plots for Middle East
plt.figure(figsize=(8, 4))
plt.subplot(1, 2, 1)
sns.scatterplot(data=filtered_df2, x='Freedom to make life choices', y='score', color='blue')
plt.title('Middle East: Score vs Freedom to Make Life Choices')
plt.xlabel('Freedom to Make Life Choices')
plt.ylabel('Score')

plt.subplot(1, 2, 2)
sns.scatterplot(data=filtered_df2, x='Generosity', y='score', color='green')
plt.title('Middle East: Score vs Generosity')
plt.xlabel('Generosity')
plt.ylabel('Score')

plt.tight_layout()
plt.show()

# Scatter plots for South Asia
plt.figure(figsize=(8, 4))
plt.subplot(1, 2, 1)
sns.scatterplot(data=filtered_df1, x='Freedom to make life choices', y='score', color='orange')
plt.title('South Asia: Score vs Freedom to Make Life Choices')
plt.xlabel('Freedom to Make Life Choices')
plt.ylabel('Score')

plt.subplot(1, 2, 2)
sns.scatterplot(data=filtered_df1, x='Generosity', y='score', color='purple')
plt.title('South Asia: Score vs Generosity')
plt.xlabel('Generosity')
plt.ylabel('Score')

plt.tight_layout()
plt.show()

# Calculate IQR and bounds for Score (South Asia region)
Q1_score = filtered_df1['score'].quantile(0.25)
Q3_score = filtered_df1['score'].quantile(0.75)
IQR_score = Q3_score - Q1_score

lower_bound_score = Q1_score - 1.5 * IQR_score
upper_bound_score = Q3_score + 1.5 * IQR_score

# Calculate IQR and bounds for Log GDP per Capita (Middle East region)
Q1_gdp = filtered_df2['Log GDP per capita'].quantile(0.25)
Q3_gdp = filtered_df2['Log GDP per capita'].quantile(0.75)
IQR_gdp = Q3_gdp - Q1_gdp

lower_bound_gdp = Q1_gdp - 1.5 * IQR_gdp
upper_bound_gdp = Q3_gdp + 1.5 * IQR_gdp

# Detect outliers for Score (South Asia)
outliers_score = filtered_df1[(filtered_df1['score'] < lower_bound_score) | (filtered_df1['score'] > upper_bound_score)]

# Detect outliers for Log GDP per Capita (Middle East)
outliers_gdp = filtered_df2[(filtered_df2['Log GDP per capita'] < lower_bound_gdp) |
                            (filtered_df2['Log GDP per capita'] > upper_bound_gdp)]

outliers = pd.concat([outliers_score, outliers_gdp])

print("Outliers in Score (South Asia):")
print(outliers_score[['Country name', 'score']])
print("\nOutliers in Log GDP per Capita (Middle East):")
print(outliers_gdp[['Country name', 'Log GDP per capita']])

# Scatter plot for Middle East
plt.figure(figsize=(8, 4))
plt.subplot(1, 2, 1)
sns.scatterplot(data=filtered_df2, x='Log GDP per capita', y='score', label='Data Points', color='blue')
sns.scatterplot(data=outliers_gdp, x='Log GDP per capita', y='score', label='Outliers', color='red', marker='X', s=100)
plt.title('Middle East: Score vs GDP per Capita')
plt.xlabel('Log GDP per Capita')
plt.ylabel('Score')
plt.legend()

# Scatter plot for South Asia
plt.subplot(1, 2, 2)
sns.scatterplot(data=filtered_df1, x='Log GDP per capita', y='score', label='Data Points', color='green')
sns.scatterplot(data=outliers_score, x='Log GDP per capita', y='score', label='Outliers', color='red', marker='X', s=100)
plt.title('South Asia: Score vs GDP per Capita')
plt.xlabel('Log GDP per Capita')
plt.ylabel('Score')
plt.legend()
plt.show()

# Create a new DataFrame combining both regions for easy comparison
filtered_df1['Region'] = 'South Asia'
filtered_df2['Region'] = 'Middle East'

combined_df = pd.concat([filtered_df1[['Country name', 'score', 'Region']], filtered_df2[['Country name', 'score', 'Region']]])

#plotting the bar graph comparing the happiness score between sount asian and middle east countries
plt.figure(figsize=(8, 4))
sns.boxplot(data=combined_df, x='Region', y='score', palette='Set2')
plt.title('Comparison of Happiness Score Distribution Between South Asia and the Middle East', fontsize=16)
plt.xlabel('Region', fontsize=12)
plt.ylabel('Happiness Score', fontsize=12)
plt.show()

"""Important information is provided by the boxplots: the median line displays the central tendency; a higher median denotes a higher average happiness score. The spread of the middle 50% of data is displayed by the interquartile range (IQR); a higher IQR denotes greater variability. Outliers outside the whiskers draw attention to high or low values, but whisker extend to the most significant and smallest values within the 15 * IQR. Greater variance in happiness levels within a region is indicated by more outliers."""