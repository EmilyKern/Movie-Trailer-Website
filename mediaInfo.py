import webbrowser
"""
The webbrowser module includes functions to open URLs in
interactive browser applications.The module includes a registry
of available browsers, in case multiple options are available
on the system. 
"""

class Movie():
    """
    This class stores movie data such as:
    movie title, movie story line, movie poster image link,
    movie trailer link
    """
    validRatings = ["G", "Y", "PG13", "R"]

    def __init__(self, movie_title, movie_storyline, poster_image, trailer_youtube):
        """
        Defining variables for the movie data using the function
        __init__ which initialiazes space and memory to remember
        details about the movie data
        """
        self.title = movie_title
        self.storyline = movie_storyline
        self.poster_image_url = poster_image 
        self.trailer_youtube_url = trailer_youtube

    def showTrailer(self):
        webbrowser.open(self.trailer_youtube_url)
        """
        To open a page in the browser, use the open() function.
        The URL is opened in a browser window, and that window
        is raised to the top of the window stack.
        """
        

 
