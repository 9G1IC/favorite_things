from django.urls import path
from .rest_views import *
from rest_framework.routers import DefaultRouter

router = DefaultRouter()
router.register('favorites', FavoriteViewSet, base_name="favorites")


urlpatterns = [
        #Create
        path("addFavorite/", FavoriteNew.as_view(), name="new_favorite"),
        #Read
        path("favorites/", FavoriteNew.as_view(), name="list_favorite"),
        #Update
        path("updateFavorite/<int:pk>", FavoriteDetail.as_view(), name="update_favorite"),
        ]

urlpatterns += router.urls
