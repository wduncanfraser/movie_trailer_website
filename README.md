# Movie Trailer Website

## Purpose
Completed as part of Project 1 for the Udacity Full Stack Nonodegree.

## Usage
1.  Clone repository: ```git clone https://github.com/wduncanfraser/movie_trailer_website.git```.
1.  Run ```python populate_db.py``` to populate the sqlite database backend.
    
    ```Note: You may also populate the DB by other means to see your own content rendered.```
1.  Run ```python entertainment_center.py``` to generate and open index.html.

## Example
[http://wduncanfraser.com/projects/movie_trailers/](http://wduncanfraser.com/projects/movie_trailers/)

## Structure
+   entertainment_center.py: Imports movie metadata from database. Calls movie_site.open_movies_page() to generate page.
+   media.py: Definition of Movie class.
+   movie_site.py: Contains templates and functions for generating movie site final html. Based on original fresh_tomatoes.py from Udacity.
+   populate_db.py: Script for populating an example database for use by entertainment_center.py
+   template.html: Website template. Imported by movie_site.py.

## External Resources
### Libraries
1.  [Materialize CSS](http://materializecss.com/)
1.  [JQuery](https://jquery.com/)

### APIs
1.  [OMDB API](http://www.omdbapi.com/): The Open Movie Database API

## Legal
Author: [W. Duncan Fraser](duncan@wduncanfraser.com)

License: [MIT License](LICENSE)