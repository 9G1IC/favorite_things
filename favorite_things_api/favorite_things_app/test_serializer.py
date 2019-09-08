from rest_framework.test import APITestCase, APIRequestFactory
from rest_framework.reverse import reverse
from favorite_things_app.rest_views import *
import json

"""
Testing Views
"""
class TestFavoriteViewSet(APITestCase):
    def setUp(self):
        self.factory = APIRequestFactory()
        self.view = FavoriteViewSet.as_view({'get': 'list'})
        self.uri = '/favorites/'

    def test_create(self):
        """Test POST method with valid data to create a new favorite """
        # Create instances
        cat = Categories.objects.create(pk=1, name="Action")
        fav = Favorites.objects.create(pk=1, title="testing", category_id=1)
        self.view = FavoriteViewSet.as_view({'post': 'create'})
        self.uri = '/addFavorite/'
        fav_json = json.dumps(fav.as_json())

        request = self.factory.post(
            reverse("new_favorite"),
            data=fav_json,
            content_type="application/json")
        response = self.view(request)
        status = response.status_code
        self.assertEqual(
            status,
            201,
            "Expected 201 received, {} {}".format(
                status,
                response.data))
