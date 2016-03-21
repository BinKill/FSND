Trailer Display - Readme

Trailer Display is a program that allows you too generate a website containing 
each movie you define in the tv.py file. Trailers will pop up upon the user 
clicking on the movie's poster.

Too add new movies you need only modify the tv.py. Create new movie instances inside
by defining the five parameters needed. (title, storyline, release_date, poster_image_url, 
and youtube_trailer_url)

ex;

new_movie = media.Movie("Title",
			"A brief description of the movie",
			"Release Date",
			"www.image.com/image.jpg",
			"www.youtube.com/watch?v=asdQE61ZHS7")

When ready too generate your wbsite simply run the tv.py file. Make sure the fresh_tomatoes.py 
and media.py files are included in the same directory as tv.py.
