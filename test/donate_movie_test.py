import unittest

from library import Library
from movie import Movie


class DonateMovieTest(unittest.TestCase):
    def test_movie_add_to_library(self):
        self.assertTrue(self.library.contains(self.library, self.movie))

    def test_copy_added(self):
        self.assertEqual(1, self.movie.get_copies())

    def setUp(self):
        self.movie = Movie()
        self.library = Library()
        self.library.donate(self.movie)


if __name__ == '__main__':
    unittest.main()
