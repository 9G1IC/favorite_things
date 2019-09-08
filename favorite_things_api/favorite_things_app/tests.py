from __future__ import unicode_literals
from django.test import TestCase
from rest_framework.test import APITestCase, APIRequestFactory
from rest_framework.reverse import reverse

from favorite_things_app.models import *
from favorite_things_app import rest_views
import json

"""
Testing Models
"""

class TestFavoriteModel(TestCase):
    def setUp(self):
        self.favorite = Favorites.objects.create()
            
    def test_compute_hash(self):
        self.assertNotEqual(self.favorite.changeLog,"","Expected hash in changeLog")

    def test_created_and_modified_date(self):
        cd = str(self.favorite.created_at).split('.')[0]
        md = str(self.favorite.modified_at).split('.')[0]
        self.assertEquals(cd,md,"Expected modified and created dates to be equal")

"""
Testing Views
"""
class TestFavoriteViewSet(APITestCase):
    def setUp(self):
        self.factory = APIRequestFactory()
        self.view = rest_views.FavoriteViewSet.as_view({'get': 'list'})
        self.uri = '/favorites/'

