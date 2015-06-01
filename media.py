"""media.py: Module for movie_trailer_website, contains Movie class"""

import webbrowser
import urllib
import json


class Movie(object):
    """This class provides a way to store movie related information.
    constructor takes movie title, imdb_id and a url for a youtube trailer as input.
    All other values are populated via OMDB API"""

    def __init__(self, title, imdb_id, trailer_youtube_url):
        # Initialize instance variables for passed parameters
        self.title = title
        self.imdb_id = imdb_id
        self.trailer_youtube_url = trailer_youtube_url

        # Query OMDB API for json response of movie data
        response = urllib.urlopen("http://www.omdbapi.com/?i=" + self.imdb_id + "&plot=short&r=json")
        movie_json = json.loads(response.read())

        # Download movie posters locally
        # IMDB does not allow hotlinking of images
        f = open('posters/' + self.imdb_id + '.jpg', 'wb')
        f.write(urllib.urlopen(movie_json['Poster']).read())
        f.close()

        # Populate remaining instance variables from json response and downloaded poster
        self.plot = movie_json['Plot']
        self.genre = movie_json['Genre']
        self.year = movie_json['Year']
        self.runtime = movie_json['Runtime']
        self.rating = movie_json['Rated']
        self.imdb_score = movie_json['imdbRating']
        self.poster_image_url = f.name

    def show_trailer(self):
        webbrowser.open(self.trailer_youtube_url)
