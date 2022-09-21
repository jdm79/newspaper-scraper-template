from difflib import restore
from venv import create
from requests import get
import random
import psycopg2
from bs4 import BeautifulSoup
import database
import requests
import datetime

db_url = "postgres://oxbvadmp:r5tJzuWI1-7XXKq1noJPVsoxFSQNfjG-@rogue.db.elephantsql.com/oxbvadmp"

papers = [
    [1, "https://www.mirror.co.uk/", "The Daily Mirror", '"h2", class_="story__title"'],
    [2, "https://www.theguardian.com/uk", "The Guardian", "'span', class_='js-headline-text'"],
    [3, "https://www.thesun.co.uk/", "The Sun", "'p', class_='teaser__subdeck'"],
    [4, "https://www.ft.com/world/uk", "The Financial Times", "'div', class_='o-teaser__heading'"],
    [5, "https://www.dailymail.co.uk/home/index.html", "The Daily Mail", "'h2', class_='linkro-darkred'"],
    [6, "https://www.thetimes.co.uk/uk", "The Times", "'h3', class_='Headline--xl'"]

]    

def scrapeHeadlines():
    scrape_results = []

    randomUrls = [ 
    "https://www.facebook.com/", 
    "https://www.google.co.uk", 
    "https://www.twitter.com"
    ]

    headers = {
        'User-Agent': 'AppleWebKit/537.36 (KHTML, like Gecko) Chrome/83.0.4103.61 Safari/537.36',
        'Referer': random.choice(randomUrls) 
        }

    fail = "Sorry but we could not get the headline for " + str(paper[2])
    timestamp = '{:%b-%d-%Y %H:%M:%S}'.format(datetime.datetime.now())
    id = paper[0]
    url = paper[1]
    newspaper = paper[2]
    element_target = paper[3]

    results = requests.get(url, headers=headers)
    soup = BeautifulSoup(results.text, "html.parser") # this can be printed out and works
    # headline_html = soup.find(paper[3])
    headline_html = soup.find(element_target) # this is not working like this

    if headline_html != None:
      headline = headline_html.text.strip()
    else:
      headline = fail 
    
    scrape_results.append({
                    'id': id,
                    'paper': newspaper,
                    'headline': headline,
                    'headline_html': headline_html
                    })
    print(scrape_results)

for paper in papers:
    scrapeHeadlines()



# connection = psycopg2.connect(db_url)

# # database.add_columns(connection) ONLY USE THIS TO ADD NEW COLUMNS
# # database.add_unique(connection)
# database.create_tables(connection)
# database.add_headline(connection, headline, url, paper, timestamp)