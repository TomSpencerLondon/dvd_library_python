import unittest


class Movie(object):
    pass


class Library(object):
    def __init__(self):
        self.catalogue = []

    def donate(self, movie):
        pass

class DonateMovieTest(unittest.TestCase):
    def test_donate_movie(self):
        movie = Movie()
        library = Library()
        library.donate(movie)
        self.assertTrue(movie in library.catalogue)

if __name__ == '__main__':
    unittest.main()