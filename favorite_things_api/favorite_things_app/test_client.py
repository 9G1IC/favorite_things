from rest_framework.test import APITestCase, APIRequestFactory,APIClient
from rest_framework.reverse import reverse
from favorite_things_app.rest_views import *

import json

class TestClientFavoriteViewSet(APITestCase):
    def setUp(self):
        self.client = APIClient()
        self.category = Categories.objects.create(pk=1, name="Action")
        self.category.save()
        self.favorite = Favorites.objects.create(pk=1,title="Setup Testing",category_id=1,rank=1)
        
    def test_client_add_post(self):
        client = self.client
        uri = '/addFavorite/'
        fav = self.favorite
        json = fav.as_json()
        response = client.post(uri,json,format="json")
        status = response.status_code
        self.assertEquals(status,200,"Expected response to be 200 but got {}, with {}".format(status,response.data))

    def test_client_add_view(self):
        client = self.client
        uri = '/addFavorite/'
        response = client.get(uri)
        #It should return dictionary with form are a key
        form = response.data
        self.assertIn('form',form,"Expected response to contain form keyword {}".format(form))

    def test_client_get(self):
        client = self.client
        uri = '/favorites/'
        response = client.get(uri)
            
        #It should return dictionary with form are a key
        form = response.data
        self.assertIn('favorite_list',form,"Expected response to contain form keyword {}".format(form))


    def test_client_get_detail(self):
        client = self.client
        uri = '/favorites/1'
        response = client.get(uri)
            
        #It should return dictionary with form are a key
        code = response.status_code
        self.assertEqual(code,301,"Expected response to redirect ")

    def test_client_update_record(self):
        client = self.client
        uri = '/updateFavorite/1'
        fav = Favorites.objects.get(pk=1)
        fav.title="Changed"
        json = fav.as_json()
        response = client.put(uri,json,format="json")
            
        status = response.status_code
        self.assertEqual(status,302,"Expected a redirection code, 302, but got {}".format(status))
            

