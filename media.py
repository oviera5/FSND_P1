import webbrowser


class Movie():

    """ This class provides a way to store movie related information. """

    def __init__(self, movie_title, movie_storyline, poster_image,
                 trailer_youtube, release_year, main_actor):
        """The constructor for the class.

        Stores movie information when an instance of the class is initalized.

        Args:
            movie_title: The title to the movie_title.
            movie_storyline: A synopsis of the movie.
            poster_image: The movie poster image acquired from a url.
            trailer_youtube: The youtube trailer url of the movie.
            release_year: The year the movie was released.
            main_actor: The main actor in the movie.
        """
        self.title = movie_title
        self.storyline = movie_storyline
        self.poster_image_url = poster_image
        self.trailer_youtube_url = trailer_youtube
        self.release_year = release_year
        self.main_actor = main_actor

    def show_trailer(self):
        """A function that opens a browser and plays a movie's trailer.

        This function is not used by the calling module, entertainment_center,
        but can be used for testing purposes.

        Args:
            movie_title: The youtube trailer url of the movie.

        """
        webbrowser.open(self.trailer_youtube_url)
