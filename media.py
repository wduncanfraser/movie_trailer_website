#!/usr/bin/env python
import webbrowser

class Movie(object):
	"""This class provides a way to store movie related information"""

	VALID_RATINGS = ["G", "PG", "PG-13", "R"]

	def __init__(self, title, storyline, post_image_url, trailer_youtube_url):
		self.title = title
		self.storyline = storyline
		self.poster_image_url = post_image_url
		self.trailer_youtube_url = trailer_youtube_url

	def show_trailer(self):
		webbrowser.open(self.trailer_youtube_url)