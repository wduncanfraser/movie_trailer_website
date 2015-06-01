-- Basic schema for storing movie metadata for Movie Trailer Website.
BEGIN TRANSACTION;
CREATE TABLE Movie (
  name	TEXT,
  imdb_id	TEXT,
  trailer_url	TEXT,
  PRIMARY KEY(name)
);
COMMIT;
