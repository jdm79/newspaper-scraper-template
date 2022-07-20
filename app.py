from venv import create
from requests import get
import psycopg2
from bs4 import BeautifulSoup
import database
import requests
import datetime

# make a timestamp here or on PostgreSQL side for each headline row
# https://stackoverflow.com/questions/38245025/how-to-insert-current-datetime-in-postgresql-insert-query
# https://www.postgresql.org/docs/current/functions-datetime.html#FUNCTIONS-DATETIME-CURRENT
# INSERT into "Group" (name,createddate) 
# VALUES ('Test', current_timestamp);


db_url = "postgres://oxbvadmp:stDxRRjicw60W6kRDQdDavS3g8_soU0Y@rogue.db.elephantsql.com/oxbvadmp"

headers = {"Accept-language": "en-US, en;q=0.5"}
url = "https://www.theguardian.com/uk"
paper = "The Guardian"

# creates dynamic url to get the current day's list
results = requests.get(url, headers=headers)
soup = BeautifulSoup(results.text, "html.parser")


timestamp = '{:%b-%d-%Y %H:%M:%S}'.format(datetime.datetime.now())
headline_html = soup.find('span', class_='js-headline-text')
headline = headline_html.text.strip()
# headline = "testing"
body = "This is the body of the article."
print(headline)

connection = psycopg2.connect(db_url)
# headline = 'Goodnight!'

# database.add_columns(connection)
database.create_tables(connection)
database.add_headline(connection, headline, url, paper, timestamp, body)





