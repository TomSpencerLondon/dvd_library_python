class Library(object):
    def __init__(self):
        self.catalogue = []

    def donate(self, movie):
        self.catalogue.append(movie)

    def contains(self, library, movie):
        return movie in library.catalogue