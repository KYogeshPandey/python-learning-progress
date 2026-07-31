# DataFrame - Methods
import numpy as nd
import pandas as pd

# Value_counts(series and Dataframes)

marks = pd.DataFrame([
    [100,80,10],
    [90,88,7],
    [87,79,9],
    [87,79,9],
    [120,95,21]
],columns=['iq','marks','Package'])
print(marks)
print(marks.value_counts())


Ipl = pd.read_csv('practice\Libraries\Pandas\Day_28(Dataframe)\ipl-matches.csv')
print(Ipl)

