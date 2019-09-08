from __future__ import unicode_literals
from django.test import TestCase

from favorite_things_app.models import *

class TestFavoriteModel(TestCase):
    def setUp(self):
        self.favorite = Favorites.objects.create()
            
    def test_compute_hash(self):
        self.assertNotEqual(self.favorite.changeLog,"","Expected hash in changeLog")
