from venv import create
from requests import get
import psycopg2
from bs4 import BeautifulSoup
import database
import requests
import datetime

db_url = "postgres://oxbvadmp:r5tJzuWI1-7XXKq1noJPVsoxFSQNfjG-@rogue.db.elephantsql.com/oxbvadmp"


fail = "Error - failed to scrape the text of this article from " 

results = []
papers = [
    {
        "id": 1,
        "url": "https://www.mirror.co.uk/",
        "paper": "Daily Mirror",
        "headline_target": "soup.find('h2', class_='story__title')"
    },
    {
        "id": 2,
        "url": "https://www.theguardian.com/uk",
        "paper": "The Guardian",
        "headline_target": """
        headline_url_html = soup.find('a', class_='fc-item__link')
        url = headline_url_html['href']
        headline_html = soup.find('span', class_='js-headline-text')
        headline = headline_html.text.strip()
        """
    }
]

def scrapeHeadlines(url, paper, headline_target):
    headers = {"Accept-language": "en-US, en;q=0.5"}
    timestamp = '{:%b-%d-%Y %H:%M:%S}'.format(datetime.datetime.now())
    results = requests.get(url, headers=headers)
    soup = BeautifulSoup(results.text, "html.parser")



    if headline_html != None:
      headline = headline_html.text.strip()
    else:
      headline = fail + paper

# creates dynamic url to get the current day's list




connection = psycopg2.connect(db_url)

# database.add_columns(connection) ONLY USE THIS TO ADD NEW COLUMNS
# database.add_unique(connection)
database.create_tables(connection)
database.add_headline(connection, headline, url, paper, timestamp)