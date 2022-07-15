from psycopg2.extras import execute_values

CREATE_HEADLINES = """CREATE TABLE IF NOT EXISTS headlines 
(headline TEXT);"""
INSERT_HEADLINE = "INSERT INTO headlines (headline) VALUES (%s);"
SELECT_ALL_HEADLINES = "SELECT * FROM headlines;"

def create_tables(connection):
    with connection:
        with connection.cursor() as cursor:
            cursor.execute(CREATE_HEADLINES)

def add_headline(connection, headline):
    with connection:
        with connection.cursor() as cursor:
            cursor.execute(INSERT_HEADLINE, (headline,))        

def get_headlines(connection):
    with connection:
        with connection.cursor() as cursor:
            cursor.execute(SELECT_ALL_HEADLINES)
            return cursor.fetchall()
