import numpy as np
import pandas as pd

# String

country = ['India','Usa','China','Japan','Australia']
print(pd.Series(country))

# Integers

runs = [33,45,54,67,100]
run_series = pd.Series(runs)
print(run_series)

# Custom Index

marks = [33,45,54,67,100]
Subjects = ['Maths','Physics','Chemistry','Biology','English']
marks_series = pd.Series(marks,index=Subjects,name = 'Marks')
print(marks_series)

# Series Attributes

# Size 
print(marks_series.size)

# dtype
print(marks_series.dtype)

# name
print(marks_series.name)

# is_unique
print(marks_series.is_unique)

# Index
print(marks_series.index)
print(run_series.index)

# Values
print(marks_series.values)
