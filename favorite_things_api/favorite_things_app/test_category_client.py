from rest_framework.test import APITestCase, APIRequestFactory,APIClient
from rest_framework.reverse import reverse
from favorite_things_app.rest_views import *
import json

class TestClientCategoryViewSet(APITestCase):
    def setUp(self):
        self.client = APIClient()
        self.category = Categories.objects.create(pk=1, name="Action")
        
    def test_client_add_post(self):
        client = self.client
        uri = '/addCategory/'
        cat = self.category
        json = cat.as_json()
        response = client.post(uri,json,format="json")
        status = response.status_code
        self.assertEquals(status,200,"Expected response to be 200 but got {}, with {}".format(status,response.data))

    def test_client_add_view(self):
        client = self.client
        uri = '/addCategory/'
        response = client.get(uri)
        #It should return dictionary with form are a key
        form = response.data
        self.assertIn('form',form,"Expected response to contain form keyword {}".format(form))

    def test_client_get_detail(self):
        client = self.client
        uri = '/updateCategory/1'
        response = client.get(uri)
        #It should return dictionary with form are a key
        form = response.data
        self.assertIn('form',form,"Expected response to contain form keyword {}".format(form))

    def test_client_update_record(self):
        client = self.client
        uri = '/updateCategory/1'
        cat = self.category
        json = cat.as_json()
        response = client.put(uri,json,format="json")
            
        status = response.status_code
        self.assertEqual(status,302,"Expected a redirection code, 302, but got {}".format(status))
            

