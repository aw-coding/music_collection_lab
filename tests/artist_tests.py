import unittest
from models.artist import Artist

class TestArtist(unittest.TestCase):
    def setUp(self):
        self.david_bowie    = Artist('David Bowie')
        self.pulp           = Artist('Pulp')
        self.the_beatles    = Artist('The Beatles')

    def test_artist_has_name(self):
        self.assertEqual('David Bowie', self.david_bowie.name)

