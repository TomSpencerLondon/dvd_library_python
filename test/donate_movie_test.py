import unittest

from library import Library
from movie import Movie

class DonateMovieTest(unittest.TestCase):
    def test_donate_movie(self):
        movie = Movie()
        library = Library()
        library.donate(movie)
        self.assertTrue(self.contains(library, movie))

    def contains(self, library, movie):
        return movie in library.catalogue


if __name__ == '__main__':
    unittest.main()