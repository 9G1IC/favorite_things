from __future__ import unicode_literals
from django.test import TestCase
from favorite_things_app.models import *

"""
Testing Category Models
"""

class TestCategoryModel(TestCase):
    def setUp(self):
        self.category = Categories.objects.create(pk=1, name="Action")
        self.category.save()
            
