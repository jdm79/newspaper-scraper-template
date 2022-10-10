# Template web scraper

This is roughly what I use to scrape headlines for [uk-headline-checker](https://www.uk-headline-checker.com/) and send results to my database (db).

You can personalise the targets to scrape and save the data to your own databases.

My version sends the data to ElephantSQL - a cloud PostgreSQL db. 

You have to make an account and set your own db url on line 11 and uncomment the db code to send data to a db. 

(My old credentials were in here in the first commit, but have since been updated. Be careful pushing code to GitHub that has your credentials in it!)

# To run, open the terminal in the root folder of this project and type:

```console
$ python3 app.py 
```

This will start the scrape and pretty print out the results to the terminal.

At the moment the db code is commented out and instead there is a list called scrape_results to which I push a dictionary for each newspaper scraped, and this is printed out to the terminal.

