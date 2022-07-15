from venv import create
from requests import get
import psycopg2
from bs4 import BeautifulSoup
import database


db_url = "postgres://oxbvadmp:stDxRRjicw60W6kRDQdDavS3g8_soU0Y@rogue.db.elephantsql.com/oxbvadmp"
db_password = "stDxRRjicw60W6kRDQdDavS3g8_soU0Y"

headers = {"Accept-language": "en-US, en;q=0.5"}
guardian_url = "https://www.theguardian.com/uk"

# # creates dynamic url to get the current day's list
# results = requests.get(guardian_url, headers=headers)

# soup = BeautifulSoup(results.text, "html.parser")

# headline_html = soup.find('span', class_='js-headline-text')
# headline = headline_html.text.strip()  



connection = psycopg2.connect(db_url)
headline = 'Hello, world!'
print(headline)
print(type(headline))

database.create_tables(connection)
database.create_headlines(connection)
database.add_headline(connection, headline)





