from psycopg2.extras import execute_values

CREATE_HEADLINES = """CREATE TABLE IF NOT EXISTS headlines 
(headline TEXT);"""
INSERT_HEADLINE = "INSERT INTO headlines (headline, url, paper, timestamp, body) VALUES (%s, %s, %s, %s, %s);"
SELECT_ALL_HEADLINES = "SELECT * FROM headlines;"

# https://www.postgresqltutorial.com/postgresql-tutorial/postgresql-add-column/
ADD_COLUMNS = """ALTER TABLE headlines
ADD COLUMN url TEXT,
ADD COLUMN paper TEXT,
ADD COLUMN timestamp TEXT,
ADD COLUMN body TEXT;"""

def create_tables(connection):
    with connection:
        with connection.cursor() as cursor:
            cursor.execute(CREATE_HEADLINES)

def add_columns(connection):
    with connection:
        with connection.cursor() as cursor:
            cursor.execute(ADD_COLUMNS)


def add_headline(connection, headline, url, paper, timestamp, body):
    with connection:
        with connection.cursor() as cursor:
            cursor.execute(INSERT_HEADLINE, (headline, url, paper, timestamp, body))        

def get_headlines(connection):
    with connection:
        with connection.cursor() as cursor:
            cursor.execute(SELECT_ALL_HEADLINES)
            return cursor.fetchall()
