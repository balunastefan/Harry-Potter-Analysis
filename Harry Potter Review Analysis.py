#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Jan 23 21:58:50 2024

@author: iuliadidu
"""
!pip install pandas

import pandas as pd

raw_csv_data = pd.read_csv("/Users/iuliadidu/Desktop/harry_potter_reviews.csv")

# Import the necessary Python libraries

import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt
import matplotlib.ticker as mtick

from PIL import Image
!pip install wordcloud 

from wordcloud import WordCloud

# Read the data from the csv file. Save it in a DataFrame.
df = pd.read_csv("/Users/iuliadidu/Desktop/harry_potter_reviews.csv")
df.head()

# Display basic information about the DataFrame

df.info()

# There are 491 rows and 8 columns
# Fortunatelly, there are no missing values

# Let's check the column types and how many of them
df.dtypes.value_counts()

# User Identifier. A unique number from 0 to 490.
# Uncorrelated with other variables.

print(df['user_id'].describe())

ax = sns.histplot(df['user_id'], color='#A0CED9')
_ = ax.set(title="'user_id' histogram")

user_sex_counts = df['user_sex'].value_counts(normalize=True)

plt.pie(
    x=user_sex_counts.values,
    labels=user_sex_counts.index,
    autopct='%1.1f%%',
    startangle=90,
)
_ = plt.title("'user_sex' Pie Chart")

ax = sns.histplot(df['user_age'], color='#A0CED9', kde=True)
_ = ax.set(title="'user_age' Histogram")

# Sort the list of unique countries by number of occurrences
sorted_countries = df['user_country'].value_counts().index

# Count Plot of the different countries in data
ax1 = sns.countplot(
    x=df['user_country'],
    color='#A0CED9',
    order=sorted_countries
)

# Create a second y-axis for percentages (%)
ax2 = ax1.twinx()

# Compute the pct of ocurrences of each country
pct_series = (df['user_country'].value_counts() / len(df)) * 100

# (Dummy) Plot to show percentages on the second y-axis
sns.lineplot(
    x=pct_series.index, 
    y=pct_series.values, 
    color='white',
    marker='o',
    ax=ax2
)
# Note that the actual lineplot's shape and form does not matter

# Send the dummy white percent plot to the back
ax2.set_zorder(1)
ax1.set_zorder(2)

# Rotate the Xlabels (45º, diagonal)
ax1.set_xticklabels(
    labels=sorted_countries,
    rotation=45, 
    ha='right',
    rotation_mode='anchor',
)
ax1.set_ylabel('Count')
ax2.set_ylabel('Percentage', color='black')

# Set the second y-axis to percentage
ax2.yaxis.set_major_formatter(mtick.PercentFormatter())

# Add the title
_ = ax1.set_title("'user_country' Count Plot")

# Sort the list of ratings ascending
rating_labels = sorted(df['rating'].unique())

# Count Plot of the different ratings in data
ax1 = sns.countplot(
    x=df['rating'],
    color='#A0CED9',
    order=rating_labels
)

# Create a second y-axis for percentages (%)
ax2 = ax1.twinx()

# Compute the pct of ocurrences of each rating
pct_series = (df['rating'].value_counts() / len(df)) * 100

# (Dummy) Plot to show percentages on the second y-axis
sns.lineplot(
    x=pct_series.index, 
    y=pct_series.values, 
    color='white',
    marker='o',
    ax=ax2
)
# Note that the actual lineplot's shape and form does not matter

# Send the dummy white percent plot to the back
ax2.set_zorder(1)
ax1.set_zorder(2)

# Rotate the Xlabels (45º, diagonal)
ax1.set_xticklabels(
    labels=rating_labels,
    rotation=45, 
    ha='right',
    rotation_mode='anchor',
)
ax1.set_ylabel('Count')
ax2.set_ylabel('Percentage', color='black')

# Set the second y-axis to percentage
ax2.yaxis.set_major_formatter(mtick.PercentFormatter())

# Add the title
_ = ax1.set_title("'rating' Count Plot")

# Let's create a wordcloud based on all the comments (reviews)
text = ' '.join(review for review in df['comment'])


# Create and generate a word cloud image:
wordcloud = WordCloud(
    background_color="white",
).generate(text)

# Display the generated image:
plt.imshow(wordcloud, interpolation='bilinear')
plt.axis("off")
plt.show()

# Sort the list of characters by the number of occurrences
sorted_fav_chars = df['favourite_character'].value_counts().index

# (Sorted) Count Plot of the different characters in data
ax1 = sns.countplot(
    x=df['favourite_character'],
    color='#A0CED9',
    order = sorted_fav_chars
)

# Create a second y-axis for percentages (%)
ax2 = ax1.twinx()

# Compute the pct of ocurrences of each character
pct_series = (df['favourite_character'].value_counts() / len(df)) * 100

# (Dummy) Plot to show percentages on the second y-axis
sns.lineplot(
    x=pct_series.index, 
    y=pct_series.values, 
    color='white',
    marker='o',
    ax=ax2
)
# Note that the actual lineplot's shape and form does not matter

# Send the dummy white percent plot to the back
ax2.set_zorder(1)
ax1.set_zorder(2)

# Rotate the Xlabels (45º, diagonal)
ax1.set_xticklabels(
    labels=sorted_fav_chars,
    rotation=45, 
    ha='right',
    rotation_mode='anchor',
)
ax1.set_ylabel('Count')
ax2.set_ylabel('Percentage', color='black')

# Set the second y-axis to percentage
ax2.yaxis.set_major_formatter(mtick.PercentFormatter())

# Add the title
_ = ax1.set_title("'favourite_character' Count Plot")