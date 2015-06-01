#!/usr/bin/env python
"""Populates an example sqlite db for storing movie metadata. Database used by entertainment_center.py."""

import sqlite3
import os.path

# Check if db file exists
if os.path.isfile('db/movies.db'):
    db_exists = True
else:
    db_exists = False

# Connect to sqlite db file
conn = sqlite3.connect('db/movies.db')
c = conn.cursor()

# If the db did not exist, populate schema
if not db_exists:
    c.execute('CREATE TABLE Movie (name TEXT, imdb_id TEXT, trailer_url TEXT, PRIMARY KEY(name))')

# Populate movie data into a list
movies = [('Super Troopers', 'tt0247745', 'https://www.youtube.com/watch?v=2-9D2qUHN-E'),
          ('Shaun of the Dead', 'tt0365748', 'https://www.youtube.com/watch?v=z-lmF5DAssU'),
          ('Gattaca', 'tt0119177', 'https://www.youtube.com/watch?v=BpzVFdDeWyo'),
          ('Serenity', 'tt0379786', 'https://www.youtube.com/watch?v=6nEAlpTb4tk'),
          ('Zombieland', 'tt1156398', 'https://www.youtube.com/watch?v=LzQ66p8Vfdk'),
          ('The Gods Must Be Crazy', 'tt0080801', 'https://www.youtube.com/watch?v=GorHLQ-jLRQ')
          ]

# Stage insertion of movie metadata into database
c.executemany('INSERT INTO Movie VALUES (?, ?, ?)', movies)

# Commit changes
conn.commit()

# Close DB connection
conn.close()