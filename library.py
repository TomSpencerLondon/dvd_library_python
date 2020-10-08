class Library(object):
    def __init__(self):
        self._catalogue = []

    def donate(self, movie):
        self._catalogue.append(movie)
        movie.add_copy()


    def contains(self, library, movie):
        return movie in library._catalogue