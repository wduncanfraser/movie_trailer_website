#!/usr/bin/env python
import fresh_tomatoes
import media

movies = []

movies.append(media.Movie("Super Troopers",
							"Five Vermont state troopers, avid pranksters with a knack for screwing up, try to save their jobs and out-do the local police department by solving a crime.",
							"http://upload.wikimedia.org/wikipedia/en/1/19/Supertrooper.jpg",
							"https://www.youtube.com/watch?v=2-9D2qUHN-E"))

movies.append(media.Movie("Shaun of the Dead",
							"A man decides to turn his moribund life around by winning back his ex-girlfriend, reconciling his relationship with his mother, and dealing with an entire community that has returned from the dead to eat the living.",
							"http://upload.wikimedia.org/wikipedia/en/e/ec/Shaun-of-the-dead.jpg",
							"https://www.youtube.com/watch?v=z-lmF5DAssU"))

movies.append(media.Movie("Gattaca",
							"A genetically inferior man assumes the identity of a superior one in order to pursue his lifelong dream of space travel.",
							"http://upload.wikimedia.org/wikipedia/en/b/bb/Gataca_Movie_Poster_B.jpg",
							"https://www.youtube.com/watch?v=BpzVFdDeWyo"))

movies.append(media.Movie("Serenity",
							"The crew of the ship Serenity tries to evade an assassin sent to recapture one of their number who is telepathic.",
							"http://upload.wikimedia.org/wikipedia/en/9/9e/Serenity_One_Sheet.jpg",
							"https://www.youtube.com/watch?v=6nEAlpTb4tk"))

movies.append(media.Movie("Zombieland",
							"A shy student trying to reach his family in Ohio, a gun-toting tough guy trying to find the last Twinkie, and a pair of sisters trying to get to an amusement park join forces to travel across a zombie-filled America.",
							"http://upload.wikimedia.org/wikipedia/en/a/a3/Zombieland-poster.jpg",
							"https://www.youtube.com/watch?v=LzQ66p8Vfdk"))

movies.append(media.Movie("The Gods Must Be Crazy",
							"A comic allegory about a traveling Bushman who encounters modern civilization and its stranger aspects, including a clumsy scientist and a band of revolutionaries.",
							"http://upload.wikimedia.org/wikipedia/en/5/59/Gods_must_be_crazyposter.jpg",
							"https://www.youtube.com/watch?v=GorHLQ-jLRQ"))

#print(media.Movie.__doc__)
#print(media.Movie.__name__)
#print(media.Movie.__module__)
fresh_tomatoes.open_movies_page(movies)