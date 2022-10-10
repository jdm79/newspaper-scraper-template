# Femicide Scraper

This is roughly what I use to scrape headlines for uk-headline-checker. 

It pushes the data to ElephantSQL - a cloud PostgreSQL database. You have to make an account and set your own db url on line 11 and uncomment the database code to send data to a db.

To run, open the terminal in the root folder of this project and type:

´´´
$ python3 app.py 
´´´

This will start the scrape and send the results to the cloud database.

At the moment the db code is commented out and instead there is a list called scraped_headlines to which I push a dictionary for each newspaper scraped and this is printed out to the terminal.

