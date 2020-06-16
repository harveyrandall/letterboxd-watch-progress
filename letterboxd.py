#!/usr/local/bin/python3

import requests
import datetime
import os
import numpy as np
import pandas as pd
from bs4 import BeautifulSoup
import utils

DIARY_LOCATION = os.path.join(
    os.path.dirname(os.path.realpath(__file__)), "data", "diary.csv"
)

def get_diary():
    username = "harveyrandall"
    today = datetime.date.today()
    year = 2020
    months = [i+1 for i in range(12)]
    base_url = "https://letterboxd.com/"
    path = f"{username}/films/diary/" #filter format: `for/year/month/day` eg for/2020/03/21 

    films = list()
    columns = ['date', 'film', 'rating', 'liked', 'rewatch']
    for month in months:
        if month > today.month:
            break
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
    utils.save_diary(films, columns, DIARY_LOCATION)
    print("Retrieved updated diary at {}".format(datetime.datetime.now()))
    return films

def get_timeseries():
    try:
        df = utils.load_diary(DIARY_LOCATION)
    except FileNotFoundError:
        get_diary()
        df = utils.load_diary(DIARY_LOCATION)
    df['date']
    watched_dict = dict(df['date'].groupby(df['date']).count().cumsum())
    today = datetime.date.today()
    days_passed = (today - datetime.date(today.year, 1, 1)).days + 1
    curr = 0
    for i in range(days_passed):
        d = (datetime.date(today.year, 1, 1) + datetime.timedelta(days=i)).isoformat()
        if watched_dict.get(d) is not None:
            watched_dict[d] = int(watched_dict[d])
            curr = int(watched_dict[d])
        else:
            watched_dict[d] = int(curr)
    return watched_dict

if __name__ == "__main__":
    get_diary()
