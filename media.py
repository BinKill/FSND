import webbrowser

class Video():
    def __init__(self, title, storyline, release_date):
        self.title = title
        self.storyline = storyline
        self.release_date = release_date

class TvShow(Video):
    def __init__(self, season, episode, tv_station):
        self.season = season
        self.episode = episode
        self.tv_station = tv_station
        
class Movie(Video):

    """Holds movie related information

    Holds and stores movie related information including the title,
    storyline, poster image url, and youtube trailer url.

    Atttributes:
        title: A string containing the title of the movie
        storyline: A string containing the storyline of the movie
        poster_image_url: A string containing a url for the post of the movie
        trailer_youtube_url: A string containing a youtube link for the movie's trailer
    """
    
    VALID_RATINGS = ["G", "PG", "PG-13", "R", "NR"]
    
    def __init__(self, title, storyline, release_date, poster, trailer):
        """Inits the Movie class

        Inititilzes the Movie class with a title instance variable,
        a storyline instance variable, a poster_image_url instance
        variable, and a trailer_youtube_url instance variable.

        Args:
            title: A string containing the title of our movie
            storyline: A string containing the storyline of our movie
            poster_image_url: A string containing a url for the post of our movie
            trailer_youtube_url: A string containing a youtube link for the movie's trailer    
        """

        self.title = title
        self.storyline = storyline
        self.release_date = release_date
        self.poster_image_url = poster
        self.trailer_youtube_url = trailer
        

    def show_trailer(self):
        """Shows a movie's trailer

        Opens a browser and navigates too a trailer of a specific
        movie.
        """
        webbrowser.open(self.trailer_youtube_url)
