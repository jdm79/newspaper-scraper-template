from difflib import restore
from venv import create
from requests import get
import random
import psycopg2
from bs4 import BeautifulSoup
import database
import requests
import datetime
from pprint import pprint

db_url = "postgres://oxbvadmp:r5tJzuWI1-7XXKq1noJPVsoxFSQNfjG-@rogue.db.elephantsql.com/oxbvadmp"

papers = [
    ["https://www.theguardian.com/uk", "The Guardian", "span", "js-headline-text", 1],
    ["https://www.mirror.co.uk/", "The Daily Mirror", "h2", "story__title", 2],
    ["https://www.thetimes.co.uk/", "The Times", "h3", "Headline--xl", 3],
    ["https://www.thesun.co.uk/", "The Sun", "p", "teaser__subdeck", 4],
    ["https://www.independent.co.uk/news/uk", "The Independent", "a", "title", 5],
    ["https://www.ft.com/world/uk", "The Financial Times", "div", "o-teaser__heading", 6],
    ["https://www.telegraph.co.uk/", "The Telegraph", "span", "list-headline__text", 7],
    ["https://www.dailymail.co.uk/home/index.html", "The Daily Mail", "h2", "linkro-darkred", 8],
    ["https://metro.co.uk/", "The Metro", "span", "colour-box", 9],
    ["https://www.standard.co.uk/news/uk", "The Evening Standard", "a", "title", 10],
    ["https://www.express.co.uk/", "The Daily Express", "h2", "", 11],
    ["https://www.dailystar.co.uk/", "The Daily Star", "a", "publication-font", 12],
    ["https://morningstaronline.co.uk/", "The Morning Star", "div", "top-story", 13],
    ["https://www.thesun.ie/", "The Irish Sun", "h2", "nk-headline-heading css-1r6h6ly", 14],
    ["https://www.heraldscotland.com/", "The Herald Scotland", "a", "mar-lead-story__link", 15],
    ["https://www.cityam.com/", "City AM", "h3", "card__title", 16]
]
scrape_results = []

def scrapeHeadlines():

    connection = psycopg2.connect(db_url)
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
    url = paper[0]
    newspaper = paper[1]
    paper_id = paper[4]

    results = requests.get(url, headers=headers)
    soup = BeautifulSoup(results.text, "html.parser")
    headline_html = soup.find(paper[2], class_=paper[3])

    if headline_html != None:
      headline = headline_html.text.strip()
    else:
      headline = fail 

    database.create_tables(connection)
    database.add_headline(connection, headline, url, newspaper, timestamp, paper_id)
    
    # this is just to print out stuff in the terminal
    scrape_results.append({
                    'id': paper_id,
                    'paper': newspaper,
                    'headline': headline
                    })

for paper in papers:
    scrapeHeadlines()

print(scrape_results)
