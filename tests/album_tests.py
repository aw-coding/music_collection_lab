import unittest
from models.album import Album

class TestAlbum(unittest.TestCase):
    def setUp(self):
        self.low = Album('Low', 'Art Rock')
        self.his_n_hers = Album('His \n Hers', "Britpop")

    def test_album_has_title(self):
        self.assertEqual('Low', self.low.title)

    def test_album_has_genre(self):
        self.assertEqual('Britpop', self.his_n_hers.genre)