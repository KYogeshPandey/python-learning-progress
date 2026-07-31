# DataFrame

import numpy as np
import pandas as pd

# Creating A  DataFrame

# using Lists
students_data = [
    [100,80,13],
    [120,89,14],
    [80,78,7]
    ]

print(pd.DataFrame(students_data,columns=['IQ','Marks','Package']))

# using Dict

student_dict = {
    'Name': ['Aman','Sumit','Yogesh','Shruti','Ankita','Dilip'],
    'IQ' : [100,90,120,80,0,0],
    'Marks' : [80,70,100,50,0,0],
    'Package' : [10,7,14,2,0,0]
}

students = pd.DataFrame(student_dict)
students.set_index('Name',inplace = True)
print(students)

# using read_csv

movies = pd.read_csv('practice\Libraries\Pandas\Day_28(Dataframe)\movies.csv')
print(movies)

Ipl = pd.read_csv('practice\Libraries\Pandas\Day_28(Dataframe)\ipl-matches.csv')
print(Ipl)

# DataFrame Attributes and Methods

# shape
# dtypes
# index
# columns
# values
# head and tail
# sample
# info
# describe
# isnull
# rename
# duplicated
# sum -> Axis Argument
# min/max/std/var

print(movies.shape)
print(movies.dtypes)
print(movies.index)
print(movies.columns)
print(students.values)
print(movies.head(7))
print(Ipl.tail(2))
print(movies.sample(5))
print(movies.columns)
print(Ipl.sample())
print(movies.info())
print(movies.describe())
print(movies.isnull().sum())
print(Ipl.duplicated().sum())
print(students.duplicated().sum())
print(students.rename(columns={'Marks':'Percentage','Package':'lpa'}))
print(students['IQ'].min())
print(students['IQ'].max())
print(students['IQ'].std())
print(students['IQ'].var())

# Selecting cols from a DataFrame
# Single cols
print(movies['title_x'])
# multiple cols
print(Ipl[['Team1','Team2','Venue','WinningTeam']])
# Select rows from a DataFrame
# iloc Singlerow
print(movies.iloc[6])
# multiple row
print(movies.iloc[0:5,2])
print(movies.iloc[[0,5,7]])
# loc
print(students.loc['Yogesh'])
print(students.loc['Aman':'Shruti':2])
print(students.iloc[0])


# Selecting Both Rows and Columns
print(movies.loc[0:3,'title_x':'poster_path'])
print(Ipl.iloc[0:3,0:3])

# Filtering a DataFrame

# Find all the final winners
# Mask = Ipl['MatchNumber'] == 'Final'
# new_df = Ipl[Mask]
# print(new_df[['Season','WinningTeam']])

print(Ipl[Ipl['MatchNumber'] == 'Final'][['Season','WinningTeam']])

print(Ipl[Ipl['SuperOver'] == 'Y'].shape[0])

# how many matches has csk won in kolkata 

print(Ipl[(Ipl['City']=='Kolkata') & (Ipl['WinningTeam'] == 'Chennai Super Kings')].shape[0])

# Toss Winner is match winner in Percentage
print(Ipl[Ipl['TossWinner'] == Ipl['WinningTeam']].shape[0]/Ipl.shape[0]*100)

# movie rating higher than 8 and number of votes > 10000
print(movies[(movies['imdb_rating'] > 8) & (movies['imdb_votes'] > 10000)].shape[0])

# Action movies rating higher than 7.5
# mask1 = movies['genres'].str.split('|').apply(lambda x : 'Action' in x)
mask1 = movies['genres'].str.contains('Action')
mask2 = movies['imdb_rating'] > 7.5
print(movies[mask1 & mask2].shape[0])

# write a function that can return the track record of two teams against each other
team1 = input("Enter First Team: ")
team2 = input("Enter Second Team: ")

temp = Ipl[((Ipl['Team1'] == team1) & (Ipl['Team2'] == team2)) |
           ((Ipl['Team1'] == team2) & (Ipl['Team2'] == team1))
           ]

wins = temp['WinningTeam'].value_counts()
total_matches = len(temp)
print(wins)


# Adding New Cols
movies['Country'] = 'India'
print(movies)

# creating columns from existing ones
# movies.dropna(inplace = True)
# movies['lead_actor'] = movies['actors'].str.split('|').apply(lambda x : x[0])
# movies

# Important DataFrame Functions

# astype
Ipl.info()
Ipl['ID'] =   Ipl['ID'].astype('int32')
print(Ipl.info())


Ipl['Season'] = Ipl['Season'].astype('category')
Ipl['Team1'] = Ipl['Team1'].astype('category')
Ipl['Team2'] = Ipl['Team2'].astype('category')

print(Ipl.info())