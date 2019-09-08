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
        self.category = Categories.objects.create(pk=1, name="Action")
        self.category.save()
        self.favorite = Favorites.objects.create(pk=1,title="Setup Testing",category_id=1)

    def test_create_with_invalid_data(self):
        """Test POST method with invalid data to create a new favorite """
        # Create instances
        fav = self.favorite

        self.view = FavoriteViewSet.as_view({'post': 'create'})
        self.uri = '/addFavorite/'
        temp = fav.as_json().pop('category')
        fav_json = json.dumps(temp)
            
        request = self.factory.post(
            reverse("new_favorite"),
            data=fav_json,
            content_type="application/json")
        response = self.view(request)
            
        status = response.status_code
            
        self.assertEqual(
            status,
            400,
            "Expected 400 received, {} {}".format(
                status,
                response.data))

    def test_create_with_valid_data(self):
        """Test POST method with invalid data to create a new favorite """
        # Create instances
        fav = self.favorite
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
            "Expected 201 received {},with error: {}".format(
                status,
                response.data))

    def test_ranking_order_should_not_repeat(self):
        """Test that the ranking order does not repeat"""
        self.view = FavoriteViewSet.as_view({'post': 'create'})
        # Create instances
        fav1 = self.favorite
        fav2 = Favorites.objects.create(pk=2, title="new", category_id=1,rank=1)
        fav2.save()

        self.uri = '/addFavorite/'
        fav_json_1 = json.dumps(fav1.as_json())
        fav_json_2 = json.dumps(fav2.as_json())
        #post the first instance
        request1 = self.factory.post(
            reverse("new_favorite"),
            data=fav_json_1,
            content_type="application/json")
        response1 = self.view(request1)
        #post the second instance
        request2 = self.factory.post(
            reverse("new_favorite"),
            data=fav_json_1,
            content_type="application/json")
        response2 = self.view(request2)
            
            
        import pdb;pdb.set_trace()
        rank1 = response1.data['rank']
        rank2 = response2.data['rank']
        self.assertNotEqual(rank1,rank2,"Expected rank1:{} not be equal to rank2:{}".format(rank1,rank2))

    def test_name_category_conflict(self):
        #Should raise an exception when the fields are same
        #cat1 = Categories.objects.create(pk=1, name="Action")
        #cat2 = Categories.objects.create(pk=2, name="Action")
        pass
        
    def test_update(self):
        """Testing PUT method with valid data to update an existing a new favorite """
        # Create instances
        fav = self.favorite
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
        #Ensure it is a success
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

        #Ensure it is modified    
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
