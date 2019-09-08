from rest_framework import serializers
from drf_writable_nested import WritableNestedModelSerializer
from favorite_things_app.models import *

class FavoriteSerializer(WritableNestedModelSerializer):

    class Meta:
        model = Favorites
        fields = '__all__'
