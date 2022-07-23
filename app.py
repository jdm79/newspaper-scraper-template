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
fail = "Error - failed to scrape "

# creates dynamic url to get the current day's list
results = requests.get(newspaper_url, headers=headers)
soup = BeautifulSoup(results.text, "html.parser")

timestamp = '{:%b-%d-%Y %H:%M:%S}'.format(datetime.datetime.now())
headline_url_html = soup.find('a', class_='fc-item__link')
url = headline_url_html['href']
headline_html = soup.find('span', class_='js-headline-text')
headline = headline_html.text.strip()

body_results = requests.get(url, headers=headers)
soup = BeautifulSoup(body_results.text, "html.parser")
body_html = soup.find('div', class_='dcr-j7ihvk')

if body_html != None:
    body = body_html.text.strip()
else:
    body = fail + paper

print(body_html)


# This will chop up the p tags but the above seems to work well enough for what we want
# body = body_html.find_all('p')
# ’print(body_html.text.strip())
# for x in body:
#     print(x.text.strip())

print(headline)
print(body)
# print(body_html)

connection = psycopg2.connect(db_url)

# database.add_columns(connection) ONLY USE THIS TO ADD NEW COLUMNS
# database.add_unique(connection)
database.create_tables(connection)
database.add_headline(connection, headline, url, paper, timestamp, body)