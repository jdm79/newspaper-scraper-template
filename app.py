from venv import create
from requests import get
import psycopg2
from bs4 import BeautifulSoup
import database
import requests
import datetime

db_url = "postgres://oxbvadmp:stDxRRjicw60W6kRDQdDavS3g8_soU0Y@rogue.db.elephantsql.com/oxbvadmp"

headers = {"Accept-language": "en-US, en;q=0.5"}
newspaper_url = "https://www.theguardian.com/uk"
paper = "The Guardian"

# creates dynamic url to get the current day's list
results = requests.get(newspaper_url, headers=headers)
soup = BeautifulSoup(results.text, "html.parser")
# print(soup)

timestamp = '{:%b-%d-%Y %H:%M:%S}'.format(datetime.datetime.now())
headline_url_html = soup.find('a', class_='fc-item__link')
url = headline_url_html['href']
headline_html = soup.find('span', class_='js-headline-text')
headline = headline_html.text.strip()
body = "This is the body of the article."
print(headline)
print(url)

connection = psycopg2.connect(db_url)

# database.add_columns(connection)
database.create_tables(connection)
database.add_headline(connection, headline, url, paper, timestamp, body)





