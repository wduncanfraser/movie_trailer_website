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

# Define template for dropdown items
dropdown_template = '''
<li><a href="#movie_{movie_count}">{movie_title}</a></li>
'''

# Define template for movie tiles
movie_tile_template = '''
<div class="col s4" id="movie_{movie_count}">
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

def create_dropdown_content(movies):
    content = ''
    count = 0
    for movie in movies:
        content += dropdown_template.format(
            movie_count=count,
            movie_title=movie.title
        )
        count += 1
    return content


def create_movie_tiles_content(movies):
    # The HTML content for this section of the page
    content = ''
    count = 0
    for movie in movies:
        # Extract the youtube ID from the url
        youtube_id_match = re.search(r'(?<=v=)[^&#]+', movie.trailer_youtube_url)
        youtube_id_match = youtube_id_match or re.search(r'(?<=be/)[^&#]+', movie.trailer_youtube_url)
        trailer_youtube_id = youtube_id_match.group(0) if youtube_id_match else None

        # Create a new row every 3 columns
        if count % 3 == 0:
            content += '<div class="row">'
        # Append the tile for the movie with its content filled in
        content += movie_tile_template.format(
            movie_count=count,
            movie_title=movie.title,
            poster_image_url=movie.poster_image_url,
            movie_plot=movie.plot,
            movie_genre=movie.genre,
            movie_year=movie.year,
            movie_runtime=movie.runtime,
            movie_rating=movie.rating,
            imdb_score=movie.imdb_score,
            trailer_youtube_id=trailer_youtube_id
        )
        # End the row every 3 columns
        if count % 3 == 2:
            content += '</div>'

        count += 1

    # End the row if it was not already ended due to being the last of 3 columns
    if count % 3 != 2:
        content += '</div>'

    return content


def open_movies_page(movies):
    # Create or overwrite the output file
    output_file = open('index.html', 'w')

    # Replace the placeholders for the movie tiles and dropdown with the actual dynamically generated content
    rendered_content = template.format(
        movie_dropdowns=create_dropdown_content(movies),
        movie_tiles=create_movie_tiles_content(movies)
    )

    # Output the file
    output_file.write(rendered_content)
    output_file.close()

    # open the output file in the browser
    url = os.path.abspath(output_file.name)
    webbrowser.open('file://' + url, new=2)  # open in a new tab, if possible
