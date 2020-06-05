import datetime 
import pandas as pd 
import numpy as np 
import matplotlib.pyplot as plt 

df = pd.read_csv('2020.csv', header=0)
fig, ax = plt.subplots()

# Generate and plot average line
today = datetime.date.today()
days_in_year = (datetime.date(today.year,12,31) - datetime.date(today.year,1,1)).days + 1
dates = [datetime.date(today.year,1,1) + datetime.timedelta(days=i) for i in range(days_in_year)]
one_avg = [i for i in range(days_in_year)]
avg = pd.Series(one_avg, dates)
avg.plot(ax=ax)

# Generate and plot current progress line
# ref: https://stackoverflow.com/questions/19324453/add-missing-dates-to-pandas-dataframe
s = pd.Series(dict(df['date'].groupby(df['date']).count().cumsum()))
s.index = pd.DatetimeIndex(s.index)
s.plot(ax=ax)
plt.show()