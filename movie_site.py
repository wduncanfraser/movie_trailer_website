"""Module for generating movie site."""

import webbrowser
import os
import re

# Check if template file exists. If not, print error and exit
if not os.path.isfile('template.html'):
    print("template.html is missing. Exiting.")
    exit()

# Open and read template
template_file = open('template.html')
template = template_file.read()
template_file.close()

# Define template for movie tiles
movie_tile_template = '''
<div class="col s4">
    <div class="card">
        <div class="card-image waves-effect waves-block waves-light">
            <img class="activator" src="{poster_image_url}" width="220">
        </div>
        <div class="card-content">
            <span class="card-title activator grey-text text-darken-4">{movie_title}<i class="mdi-navigation-more-vert right"></i></span>
            <a class="waves-effect waves-light btn modal-trigger" href="#trailer" data-trailer-youtube-id="{trailer_youtube_id}" id="trailer_button">Watch Trailer</a>
        </div>
        <div class="card-reveal">
            <span class="card-title grey-text text-darken-4">{movie_title}<i class="mdi-navigation-close right"></i></span>
            <p>Plot: {movie_plot}</p>
            <p>Genre: {movie_genre}</p>
            <p>Year: {movie_year}</p>
            <p>Runtime: {movie_runtime}</p>
            <p>Rating: {movie_rating}</p>
            <p>IMDB Score: {imdb_score}</p>
        </div>
    </div>
</div>
'''
#
def create_movie_tiles_content(movies):
    # The HTML content for this section of the page
    content = ''
    for movie in movies:
        # Extract the youtube ID from the url
        youtube_id_match = re.search(r'(?<=v=)[^&#]+', movie.trailer_youtube_url)
        youtube_id_match = youtube_id_match or re.search(r'(?<=be/)[^&#]+', movie.trailer_youtube_url)
        trailer_youtube_id = youtube_id_match.group(0) if youtube_id_match else None

        # Append the tile for the movie with its content filled in
        content += movie_tile_template.format(
            movie_title = movie.title,
            poster_image_url = movie.poster_image_url,
            movie_plot = movie.plot,
            movie_genre = movie.genre,
            movie_year = movie.year,
            movie_runtime = movie.runtime,
            movie_rating = movie.rating,
            imdb_score = movie.imdb_score,
            trailer_youtube_id=trailer_youtube_id
        )
    return content

def open_movies_page(movies):
  # Create or overwrite the output file
  output_file = open('index.html', 'w')

  # Replace the placeholder for the movie tiles with the actual dynamically generated content
  rendered_content = template.format(movie_tiles=create_movie_tiles_content(movies))

  # Output the file
  output_file.write(rendered_content)
  output_file.close()

  # open the output file in the browser
  url = os.path.abspath(output_file.name)
  webbrowser.open('file://' + url, new=2) # open in a new tab, if possible