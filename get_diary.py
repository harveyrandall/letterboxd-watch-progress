import requests
from bs4 import BeautifulSoup

base_url = "https://letterboxd.com/"
username = "harveyrandall"
page_num = 1
path = f"{username}/films/diary/page/"

entries = dict()
current_month = None
current_year = None
while True:
    html = requests.get(f"{base_url}{path}{page_num}").content
    soup = BeautifulSoup(html, 'html.parser')    
    entries = soup.find_all('tr', class_='diary-entry-row')
    if len(entries) == 0:
        break

    for entry in entries:
        cells = entry.contents[1:-1]
        month = cells[0].find('strong')
        year = cells[0].find('small')
        if month not None and year not None:
            current_month = month.text
            current_year = year.text
        day = int(cells[2].find('a').text)
    
    #total_entries += entries
    page_num += 1
    
'''
for entry in html.find_all('tr', class_='diary-entry-row'):
    for idx, child in enumerate(entry.children):
        print(idx, child)
    break
'''