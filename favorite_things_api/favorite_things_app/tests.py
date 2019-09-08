from __future__ import unicode_literals
from django.test import TestCase

from favorite_things_api import *

    
class TestFavoriteModel(TestCase):
    def setUp(self):
        self.category = Categories.object.create()
        self.favorite = Favorites.objects.create()
            
    
    def test_compute_hash(self):
        self.assertIsNotEmpty(self.favorite.changeLog,"","Expected hash")
