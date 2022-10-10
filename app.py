from difflib import restore
from venv import create
from requests import get
import random
import psycopg2
from bs4 import BeautifulSoup
import database
import requests
import datetime
from pprintpp import pprint as pp

# Put your cloud database url here (or use more secure files to store your credentials)
db_url = ""


fail = "Error - failed to scrape the text of this article from " 

# These are the papers I scrape, as elements of a Python list. the last two are the variables needed for the Beautiful Soup find function
papers = [
    [1, "https://www.mirror.co.uk/", "The Daily Mirror", "h2", "story__title"],
    [2, "https://www.theguardian.com/uk", "The Guardian", "span", "js-headline-text"],
    [3, "https://www.thesun.co.uk/", "The Sun", "p", "teaser__subdeck"],
    [4, "https://www.ft.com/world/uk", "The Financial Times", "div", "o-teaser__heading"],
    [5, "https://www.dailymail.co.uk/home/index.html", "The Daily Mail", "h2", "linkro-darkred"],
    [6, "https://www.thetimes.co.uk/", "The Times", "h3", "Headline--xl"]

]

# This is an empty Python list which will be populated each scrape in order to print and look at the results. 
# Is for testing purposes only and has nothing to do with the database.
scrape_results = []


# define function which will then be used in a for loop at the bottom of this file to scrape all the websites
def scrapeHeadlines():

    # This needs to be uncommented to save data to a database
    # connection = psycopg2.connect(db_url)

    # This is in order to sneak past some websites (although most are fine without having to use this)
    randomUrls = [ 
    "https://www.facebook.com/", 
    "https://www.google.co.uk", 
    "https://www.twitter.com"
    ]

    # Use random referrers
    headers = {
        'User-Agent': 'AppleWebKit/537.36 (KHTML, like Gecko) Chrome/83.0.4103.61 Safari/537.36',
        'Referer': random.choice(randomUrls) 
        }

    # 
    fail = "Sorry but we could not get the headline for " + str(paper[2])
    timestamp = '{:%b-%d-%Y %H:%M:%S}'.format(datetime.datetime.now())
    id = paper[0]
    url = paper[1]
    newspaper = paper[2]

    # The scrape begins here. The http request is fired off to the target website and the results are saved
    results = requests.get(url, headers=headers)
    
    # We then parse the results to text, but we still have the whole page here. We need to grab the exact part of this page
    soup = BeautifulSoup(results.text, "html.parser")

    # Here we target the exact part (or element) of the page using the find function. 
    # The below code would look like the following if I hard-coded it: headline_html = soup.find("h3", class_="Headline--xl")
    headline_html = soup.find(paper[3], class_=paper[4])

    # Very basic error catch here to check if the scrape worked. If it returns nothing, the fail message will be returned instead. 
    # if not, the strip function will clean up the data
    if headline_html != None:
      headline = headline_html.text.strip()
    else:
      headline = fail 

    # Uncomment the db code below to send the data to your PostgreSQL database
    # database.create_tables(connection)

    # database.add_headline(connection, headline, url, newspaper, timestamp)

    # This is just for testing purposes. 
    # It will send a dictionary/Python object (I came from JavaScript) to the scrape_results list.
    scrape_results.append({
                    'id': id,
                    'paper': newspaper,
                    'headline': headline
                    })

# Loop through the papers list which is at the top of this file
# use the scrapeHeadlines function on each newspaper
for paper in papers:
    scrapeHeadlines()

# Pretty print out to the terminal the results
pp(scrape_results)
