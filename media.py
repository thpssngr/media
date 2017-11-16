import webbrowser

class Movie():
    '''This class provides a way to store metadata for movies'''
    VALID_RATINGS = ["G", "PG", "PG-13", "R"]
    def __init__(self, movie_title, movie_storyline, movie_releaseyear, poster_image, trailer_youtube):
        '''initializing the Movie class with all required attributes'''
        self.title = movie_title
        self.storyline = movie_storyline
        self.releaseyear = movie_releaseyear
        self.poster_image_url = poster_image
        self.trailer_youtube_url = trailer_youtube

    def show_trailer(self):
        '''opening a new web browser window with the youtube triler url'''
        webbrowser.open_new(self.trailer_youtube_url)
