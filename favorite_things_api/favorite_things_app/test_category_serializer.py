from rest_framework.test import APITestCase, APIRequestFactory,APIClient

from rest_framework.reverse import reverse
from favorite_things_app.rest_views import *
import json

"""
Testing Views
"""
class TestCategoryViewSet(APITestCase):
    def setUp(self):
        self.factory = APIRequestFactory()
        self.uri = '/categories/'
        self.category = Categories.objects.create(pk=1, name="Action")
        self.category.save()

    def test_create_with_invalid_data(self):
        """Test POST method with invalid data to create a new favorite """
        # Create instances

        self.view = FavoriteViewSet.as_view({'post': 'create'})
        self.uri = '/addCategory/'
        cat = Categories.objects.create()
        cat_json = json.dumps(cat.as_json())
            
        request = self.factory.post(
            reverse("new_category"),
            data=cat_json,
            content_type="application/json")
        response = self.view(request)
            
        status = response.status_code
            
        self.assertEqual(
            status,
            400,
            "Expected 400 received, {} {}".format(
                status,
                response.data))
