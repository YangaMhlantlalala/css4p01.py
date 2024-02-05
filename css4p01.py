# -*- coding: utf-8 -*-
"""
Created on Mon Feb  5 13:26:41 2024

@author: yanga
"""
#Cleaning the data

import pandas as pd

df=pd.read_csv("movie_dataset.csv")
print(df)

print(df.info())
#Filling the missing cells

#Revenue (Millions)
y = df["Revenue (Millions)"].mean()
df["Revenue (Millions)"].fillna(y, inplace = True)

#Metascore
p = df["Metascore"].mean()
df["Metascore"].fillna(p, inplace = True)

print(df.info())

#QUESTION 1
#Highest Rating
import pandas as pd

Highest_Rated = df['Rating'].max()
print(Highest_Rated)
Highest_Rating=9.0

#a movie with a 9.0 rating (highest rating)
print(df['Rating'])
df[df['Rating']==9]
#The movie with index=54, Rank=55 and rating=9 is the The Dark Knight

#QUESTION2
#Average Revenue
import pandas as pd

#Method 1
sum_of_Revenue=pd.to_numeric(df['Revenue (Millions)'],errors='coerce').sum()
print(sum_of_Revenue)
sum_of_Revenue=82956.37614678899
len=1000
avg= sum_of_Revenue/len
print(avg)
#avg=82.95637614678898

#Method 2
avg_of_Revenue=pd.to_numeric(df['Revenue (Millions)'],errors='coerce').mean()
print("Average Revenue of All Movies: ${:,.2f}".format(avg_of_Revenue))


#QUESTION 3
# 'Year' column to datetime format
df['Year'] = pd.to_datetime(df['Year'], format='%Y')

# filtering movies released from 2015 to 2017
df1 = df[(df['Year'] >= '2015-01-01') & (df['Year'] <= '2017-12-31')]

# Calculating the average revenue of movies from 2015 to 2017
avg_revenue_2015_to_2017 = df1['Revenue (Millions)'].mean()
print(f"The average revenue of movies from 2015 to 2017 is {avg_revenue_2015_to_2017:.2f} million dollars.")


#QUESTION 4

df['Year'] = pd.to_datetime(df['Year'], format='%Y')

# filtering movies released from 2015 to 2017
df1 = df[(df['Year'] >= '2015-01-01') & (df['Year'] <= '2017-12-31')]



#Movies released in 2016
import pandas as pd
#Extract the year and store it in a new column 'Year_Only'

df['Year'] = df['Year'].dt.year
print(df['Year'])

movies_2016 = (df['Year'] == 2016).sum()
print(f"There were {movies_2016:.2f} released in 2016.")

#QUESTION 5

import pandas as pd

#movies directed by Christopher Nolan
movies_by_Christopher_Nolan=(df['Director']== 'Christopher Nolan').sum()
print(movies_by_Christopher_Nolan)
print(f"The movies directed by Christopher Nolan is {movies_by_Christopher_Nolan:.2f}")



#QUESTION 6
import pandas as pd

#Movies with 8.0 rationg
movies_8= (df['Rating'] >= 8.0).sum()
print(movies_8)
print(f"The movies with 8.0 rating are {movies_8:.2f}")

#QUESTION 7

import pandas as pd

# movies directed by Christopher Nolan
nolan_movies = df[df['Director'] == 'Christopher Nolan']

# median rating of movies directed by Christopher Nolan
median_rating_nolan_movies = nolan_movies['Rating'].median()
print(f"The median rating of movies directed by Christopher Nolan is {median_rating_nolan_movies}.")


#QUESTION 8

import pandas as pd

#Average year rating
yearly_average_rating= df.groupby('Year')['Rating'].mean()
print(yearly_average_rating)

#Highest average year rating
year_highest_avg_rating = yearly_average_rating.idxmax()
print(f"The the year with the highest average rating is {year_highest_avg_rating}.")


#QUESTION 9
# % increase 
import pandas as pd

#Calculating the number of movies made in 2006 and 2016
movies_2006=(df['Year'] == 2006).sum()
print(f"There were {movies_2006} movies made in 2006.")

movies_2016 = (df['Year'] == 2016).sum()
print(f"There were {movies_2016} movies made in 2016.")

# Calculate the percentage increase
percentage_increase = (movies_2016 - movies_2006) / (movies_2006) * 100

print(f"There percentage increase of movies made in 2006 and 2016 is {percentage_increase} %")


#QUESTION 10
import pandas as pd

# Spliting the multiple actors in the "Actors" column and creating a new DataFrame
actors_df = df['Actors'].str.split(', ', expand=True)

# Restructuring the dataFrame to have one column for each actor
actors_list = actors_df.values.flatten()

#Count the occurrences of each actor
actors_count = pd.Series(actors_list).value_counts()

# Get the most common actor
most_common_actor = actors_count.idxmax()

print(f"The most common actor in all the movies is: {most_common_actor}")

#QUESTION 11
#Unique Genres
import pandas as pd

# Spliting the genres into lists
genres_lists = df['Genre'].str.split(', ')

# creating a single list of all genres
all_genres = [genre for sublist in genres_lists.dropna() for genre in sublist]

# Count the unique genres
unique_genres = len(set(all_genres))
print(f"The number of unique genres in the dataset is: {unique_genres}")


#QUESTION 12

import pandas as pd

#correlation of the numerical features

#Filtering columns with numerical features
numerical_df = df.select_dtypes(include=['number'])
df2=numerical_df
print(df2)

#Correlating matrix printing
correlation_matrix = df2.corr()
print(correlation_matrix)

#Printing insights

#Plotting the correlation Heatmap
import seaborn as sns
import matplotlib.pyplot as plt

plt.figure(figsize=(10, 8))
sns.heatmap(correlation_matrix, annot=True, cmap='coolwarm', linewidths=.5)
plt.title('Correlation Heatmap')
plt.show()

#INSIGHTS

#A moderate correlation between the votes and metascore
#Moderate positive correlation between rating and revenue
#A positive correlation between revenue and metascore
#Weak positive correlation between rating and runtime
#A moderate correlation between votes and rating
#Weak correlation between rank and runtime
