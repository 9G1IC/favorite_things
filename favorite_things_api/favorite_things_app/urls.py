from django.urls import path
from .rest_views import *
from rest_framework.routers import DefaultRouter

router = DefaultRouter()
router.register('favorites', FavoriteViewSet, base_name="favorites")


urlpatterns = [
        path("addFavorite/", FavoriteNew.as_view(), name="new_favorite"),
        ]
urlpatterns += router.urls