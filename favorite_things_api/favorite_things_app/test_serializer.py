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

    def test_name_category_conflict(self):
        #Should raise an exception when the fields are same
        #cat1 = Categories.objects.create(pk=1, name="Action")
        #cat2 = Categories.objects.create(pk=2, name="Action")
        pass
        
    def test_update(self):
        """Testing PUT method with valid data to update an existing a new favorite """
        # Create instances
        cat = Categories.objects.create(pk=1, name="Action")
        fav = Favorites.objects.create(pk=1,title="Original", category_id=1)
        #save
        fav.save()
        self.view = FavoriteViewSet.as_view({'put': 'update'})
        #modify the fav_json
        temp = fav.as_json()
        temp['title'] = "modified"
        fav_json = json.dumps(temp)
        self.uri = '/updateFavorite/'

        request = self.factory.put(
            reverse("update_favorite",args=[1]),
            data=fav_json,
            content_type="application/json")

        response = self.view(request, pk=1)
        status = response.status_code
        body = response.data
        self.assertEqual(
            status,
            200,
            "Expected 200 received, {} {}".format(
                status,
                response.data))
        from datetime import datetime
        # Using [1] due to the time interval
        ct = body['created_at'].split('.')[1]
        mt = body['modified_at'].split('.')[1]
        # Check the hashes too
        fh = fav.changeLog
        mh = body['changeLog']

        self.assertNotEqual(
            ct,
            mt,
            "Expected Created time not to equal updated time received, {} {}".format(
                ct,
                mt))
        self.assertNotEqual(
            fh,
            mh,
            "Expected Created Log not to equal updated Log received, {} {}".format(
                fh,
                mh))
