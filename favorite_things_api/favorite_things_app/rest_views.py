from rest_framework import generics, viewsets
from rest_framework.renderers import TemplateHTMLRenderer
from rest_framework.response import Response
from django.shortcuts import get_object_or_404, redirect
from django.forms import modelformset_factory

# Import local modules
from favorite_things_app.models import *
from favorite_things_app.rest_serializers import *

class FavoriteNew(generics.CreateAPIView):
    pass

class FavoriteViewSet(viewsets.ModelViewSet):
    queryset = Favorites.objects.order_by("rank")
    serializer_class = FavoriteSerializer
