from django.urls import path
from .rest_views import *
from rest_framework.routers import DefaultRouter

router = DefaultRouter()
router.register('favorites', FavoriteViewSet, base_name="favorites")
router.register('categories', FavoriteViewSet, base_name="categories")


urlpatterns = [
        #Create
        path("addFavorite/", FavoriteNew.as_view(), name="new_favorite"),
        #Read
        path("favorites/", FavoriteNew.as_view(), name="list_favorites"),
        #Update
        path("updateFavorite/<int:pk>", FavoriteDetail.as_view(), name="update_favorite"),
        #Detail
        path("favorites/<int:pk>", FavoriteDetail.as_view(), name="get_favorite"),

        #Category
        path("addCategory/", CategoryNew.as_view(), name="new_category"),
        ]

urlpatterns += router.urls
