import requests
import datetime
import numpy as np
import pandas as pd
from bs4 import BeautifulSoup

username = "harveyrandall"
year = 2020
months = [i+1 for i in range(12)]
base_url = "https://letterboxd.com/"
path = f"{username}/films/diary/" #filter format: `for/year/month/day` eg for/2020/03/21 

films = list()
columns = ['date', 'film', 'rating', 'liked', 'rewatch']
for month in months:
    filter_range = f"for/{year}/{month}"
    html = requests.get(f'{base_url}{path}{filter_range}').content
    soup = BeautifulSoup(html ,'html.parser')

    entries = soup.find_all('tr', class_='diary-entry-row')
    if len(entries) == 0:
        continue

    for entry in entries:
        cols = entry.contents[1::2]
        day = int(cols[1].find('a').text)
        dt = datetime.date(year, month, day)
        film_name = cols[2].find('h3').find('a').text
        rating = float(cols[4].find('input', class_="rateit-field")['value'])/2
        liked = True if cols[5].find('span', class_='icon-liked') else False
        rewatch = not ("icon-status-off" in cols[6]['class'])
        films.append([dt, film_name, rating, liked, rewatch])
        
df = pd.DataFrame(np.array(films), columns=columns)
df.sort_values(by=['date'], inplace=True)
df.reset_index(inplace=True, drop=True)
with open('2020.csv', 'w') as f:
    df.to_csv(f)