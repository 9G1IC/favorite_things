from __future__ import unicode_literals
from django.test import TestCase
from favorite_things_app.models import *

"""
Testing Models
"""

class TestFavoriteModel(TestCase):
    def setUp(self):
        self.favorite = Favorites.objects.create(category_id=1)
        self.category = Categories.objects.create(pk=1, name="Action")
        self.category.save()
            
    def test_compute_hash(self):
        self.assertNotEqual(self.favorite.changeLog,"","Expected hash in changeLog")

    def test_created_and_modified_date(self):
        cd = str(self.favorite.created_at).split('.')[0]
        md = str(self.favorite.modified_at).split('.')[0]
        self.assertEquals(cd,md,"Expected modified and created dates to be equal")
