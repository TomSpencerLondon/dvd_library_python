class Library(object):
    def __init__(self):
        self.catalogue = []

    def donate(self, movie):
        self.catalogue.append(movie)
        movie.add_copy()


    def contains(self, library, movie):
        return movie in library.catalogue