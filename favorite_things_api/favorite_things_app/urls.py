from django.urls import path
from .rest_views import *
from rest_framework.routers import DefaultRouter

router = DefaultRouter()
router.register('favorites', FavoriteViewSet, base_name="favorites")
router.register('categories', CategoryViewSet, base_name="categories")


urlpatterns = [
        #Create
        path("addFavorite/", FavoriteList.as_view(), name="new_favorite"),
        #Read
        path("favorites/", FavoriteList.as_view(), name="list_favorites"),
        #Update
        path("updateFavorite/<int:pk>", FavoriteDetail.as_view(), name="update_favorite"),
        #Detail
        path("favorites/<int:pk>", FavoriteDetail.as_view(), name="get_favorite"),

        #Category
        #Create
        path("addCategory/", CategoryNew.as_view(), name="new_category"),
        #Read
        path("categories/", CategoryNew.as_view(), name="list_categories"),
        #Update
        path("updateCategory/<int:pk>", CategoryDetail.as_view(), name="update_category"),
        ]

urlpatterns += router.urls
