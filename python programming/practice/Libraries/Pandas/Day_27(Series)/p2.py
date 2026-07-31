# Series Using read_csv
import pandas as pd
import numpy as np

# With one column
subs = pd.read_csv(r'C:\Users\HP\Desktop\python progamming\practice\Libraries\Day_27(Pandas)\subs.csv').squeeze('columns')
print(subs)

# With two column
kohli = pd.read_csv(r'C:\Users\HP\Desktop\python progamming\practice\Libraries\Day_27(Pandas)\kohli_ipl.csv',index_col = 'match_no').squeeze('columns')
print(kohli)

movies = pd.read_csv(r'C:\Users\HP\Desktop\python progamming\practice\Libraries\Day_27(Pandas)\bollywood.csv',index_col = 'movie').squeeze('columns')
print(movies)


# Series Methods
# Head and Tail
print(subs.head(3))
print(subs.tail(3))

# Sample

print(movies.sample(5))

# value_counts
print(movies.value_counts())

# Sort_values
print(kohli.sort_values())

#sort_index
movies.sort_index(inplace = True)
print(movies)

# Series Maths Methods
# Count and Sum and product
print(kohli.count())  
print(subs.sum())

print(subs.product())

# Mean / Median / Mode / Standard Deviation / variance
print(kohli.mean())
print(subs.median())
print(subs.mode())
print(subs.std())
print(subs.var())

# Min / max
print(subs.min())
print(subs.max())

# Describe
print(kohli.describe())


# Series Indexing and Slicing
# Integer Indexing

x = pd.Series([1,2,3,4,5])
print(x[0])

'''negative indexing is not supported in series, It only works for text based indexing.'''

print(movies['3 Idiots'])
print(movies[0])

# Slicing
print(subs[0:3])
print(kohli[5:10])

print(kohli[-5:-1])
print(kohli[-10:-5])
print(kohli[::2])


# Fancy Indexing
print(subs[[0,2,4]])


# Editing In series
marks_series = pd.Series([10,20,30,40,50])
marks_series[0] = 100
print(marks_series)

# What if index does not exist in series
marks_series['Sst'] = 90
print(marks_series)

# Slicing and Editing
marks_series[1:3] = [200,300]
print(marks_series)

# using index label
movies['2 States'] = "Alia Bhatt"
print(movies)

# Series with python functonalities

# len/type/dir/sorted/max/min

print(len(subs))
print(type(subs))
print(dir(subs))
print(sorted(subs))
print(max(subs))
print(min(subs))

# type conversion
print(list(subs))

# membership operators

print('2 States' in movies)
print('Alia Bhatt' in movies.values)

# Looping
for i in movies.index:
    print(i)

# Relational Operators
print(kohli >= 50)

# Boolean Indexing In series
# Find no of 100's and 50's scored by kohli in ipl
print(kohli[kohli >= 50].size)
print(kohli[kohli >= 100].size)
print(kohli[kohli == 0].size)
print(subs[subs > 200].size)

# Find actors who had worked in miore than 20 films in last year

num_movies = movies.value_counts()
print(num_movies[num_movies > 20])

# Plotting graph
import matplotlib.pyplot as plt
subs.plot()
# plt.show()
movies.value_counts().head(20).plot(kind='pie')
# plt.show()



# Some other functions of Pandas Series

# astype
import sys 
print(sys.getsizeof(kohli))

# Between
print(kohli[kohli.between(51,99)].size)

# clip

print(subs.clip(100,200))

# drop_duplicates
temp = pd.Series([1,1,2,1,4,2,5,3,4,5,3])
print(temp.drop_duplicates(keep = 'last'))

print(temp.duplicated().sum())
print(kohli.duplicated().sum())

# isnull
temp = pd.Series([1,2,3,np.nan,5,np.nan,7,8,9,np.nan])
print(temp)
print(temp.size)
print(temp.count())

print(temp.isnull().sum())
print(kohli.isnull().sum())


# dropna
print(temp.dropna())

# fillna
print(temp.fillna(temp.mean()))


# isin
print(kohli[(kohli == 49) | (kohli == 99)])
print(kohli[kohli.isin([49,78,89,67])])


# apply
print(movies.apply(lambda x : x.split()[0].upper()))

print(subs.apply(lambda x :'good day' if x > subs.mean() else 'bad day'))


# copy
kohli
new = kohli.head()
new[1] = 100
print(new)
print(kohli)

new2 = kohli.head().copy()
new2[1] = 200
print(new2)
print(new)
print(kohli)