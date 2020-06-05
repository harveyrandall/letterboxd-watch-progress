import datetime 
import pandas as pd 
import numpy as np 
import matplotlib.pyplot as plt 
from collections import OrderedDict

df = pd.read_csv('2020.csv', header=0)
fig, ax = plt.subplots()

today = datetime.date.today()
days_in_year = (datetime.date(today.year,12,31) - datetime.date(today.year,1,1)).days + 1
avg = pd.Series({(datetime.date(today.year,1,1) + datetime.timedelta(days=i)): i+1 for i in range(days_in_year)})
avg.plot(ax=ax, label="Film a day")

#watched_df = pd.DataFrame(df['date'].groupby(df['date']).count().cumsum())
watched_dict = dict(df['date'].groupby(df['date']).count().cumsum())
watched_dict_year = dict()
curr = 0
for i in range(days_in_year):
    d = (datetime.date(today.year, 1, 1) + datetime.timedelta(days=i)).isoformat()
    if watched_dict.get(d) is not None:
        watched_dict_year[d] = watched_dict[d]
        curr = watched_dict[d]
    else:
        watched_dict_year[d] = curr
watched = pd.Series(watched_dict_year)
watched.index = pd.DatetimeIndex(watched.index)
watched.plot(ax=ax, label="Films watched")

ax.set_title("Film progress for the year so far")
ax.set_xlim(datetime.date(today.year,1,1), datetime.date(today.year,12,31))
ax.set_ylim(0, days_in_year)
ax.set_yticks(np.arange(0, days_in_year, 30))
ax.legend()
plt.show()
'''
# Generate and plot average line
today = datetime.date.today()
days_in_year = (datetime.date(today.year,12,31) - datetime.date(today.year,1,1)).days + 1
dates = [datetime.date(today.year,1,1) + datetime.timedelta(days=i) for i in range(days_in_year)]
one_avg = [i for i in range(days_in_year)]
avg = pd.Series(one_avg, dates)
avg.plot(ax=ax, label="Film a day")

# Generate and plot current progress line
# ref: https://stackoverflow.com/questions/19324453/add-missing-dates-to-pandas-dataframe
s = pd.Series(dict(df['date'].groupby(df['date']).count().cumsum()))
s.index = pd.DatetimeIndex(s.index)
s.plot(ax=ax, label="Films watched")

# Adjust plot appearance 
ax.set_title("Film progress for the year so far")
ax.set_xlim(datetime.date(today.year,1,1), datetime.date(today.year,12,31))
ax.set_ylim(0, days_in_year)
ax.set_yticks(np.arange(0, days_in_year, 30))
ax.legend()
plt.show()
'''