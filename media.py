import webbrowser

class Movie():
    '''This class provides a way to store metadata for movies'''
    VALID_RATINGS = ["G", "PG", "PG-13", "R"]
    def __init__(self, movie_title, movie_releaseyear, movie_storyline, poster_image, trailer_youtube):
        self.title = movie_title
        self.storyline = movie_storyline
        self.releaseyear = movie_releaseyear
        self.poster_image_url = poster_image
        self.trailer_youtube_url = trailer_youtube

    def show_trailer(self):
        webbrowser.open_new(self.trailer_youtube_url)
