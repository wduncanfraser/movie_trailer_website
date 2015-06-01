#!/usr/bin/env python
""""""
import sqlite3
import os.path
import fresh_tomatoes
import media

# Check if db file exists. Exit if not found.
if not os.path.isfile('db/movies.db'):
    print("Database file not present, exiting.")
    exit()

# Connect to sqlite db file
conn = sqlite3.connect('db/movies.db')
c = conn.cursor()

# Create blank list for storing movies
movies = []

# Query DB for all movie entries. Append each entry to movies list
for row in c.execute('SELECT * from Movie'):
    movies.append(media.Movie(row[0], row[1], row[2]))

# Pass movie list to fresh_tomatoes
fresh_tomatoes.open_movies_page(movies)
