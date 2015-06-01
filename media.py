"""media.py: Module for movie_trailer_website, contains Movie class"""

import webbrowser
import urllib
import json


class Movie(object):
    """This class provides a way to store movie related information"""

    def __init__(self, title, imdb_id, trailer_youtube_url):
        self.title = title
        self.imdb_id = imdb_id
        self.trailer_youtube_url = trailer_youtube_url

        response = urllib.urlopen("http://www.omdbapi.com/?i=" + self.imdb_id + "&plot=short&r=json")
        movie_json = json.loads(response.read())

        self.rating = movie_json['Rated']
        self.plot = movie_json['Plot']
        self.poster_image_url = movie_json['Poster']

    def show_trailer(self):
        webbrowser.open(self.trailer_youtube_url)
