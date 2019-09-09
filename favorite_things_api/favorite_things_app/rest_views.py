from rest_framework import generics, viewsets
from rest_framework.renderers import TemplateHTMLRenderer
from rest_framework.response import Response
from django.shortcuts import get_object_or_404, redirect
from django.forms import modelformset_factory

# Import local modules
from favorite_things_app.models import *
from favorite_things_app.forms import *
from favorite_things_app.rest_serializers import *

header = "header.html"
footer = "footer.html"
title = "Favorite App"

class CategoryNew(generics.ListCreateAPIView):
    template_name = "category/addCategory.html"
    serializer_class = CategorySerializer
    renderer_classes = [TemplateHTMLRenderer]

    def get(self,request,*args,**kwargs):
        form = CategoryForm()
        return Response({"title": title, "header": header, "footer": footer,"form": form})

    def create(self,request,*args,**kwargs):
        data = request.data
        serializer = CategorySerializer(data=data)
        if not serializer.is_valid():
            #Use the same form to display the errors
            self.template_name = "category/categoryList.html"
            return Response({"title": title, "header": header, "footer": footer,
		"category_list": [{"title":"Unable to save","description":str(serializer.error_messages)}] })
        serializer.save()
        queryset = Categories.objects.all()
        #show the list
        self.template_name = "category/categoryList.html"
        return Response({"title": title, "header": header, "footer": footer,"category_list": queryset })

class CategoryDetail(generics.RetrieveUpdateDestroyAPIView):
    template_name = "category/categoryDetail.html"
    serializer_class = CategorySerializer
    renderer_classes = [TemplateHTMLRenderer]

    #Read
    def get(self, request, pk):
        item = get_object_or_404(Categories, pk=pk)
        form = CategoryForm(instance=item)
        return Response({"title": title, "header": header, "footer": footer,
            "form": form})
    #update 
    def update(self,request,pk):
        item = get_object_or_404(Categories, pk=pk)
        serializer = CategorySerializer(item, data=request.data)
        if not serializer.is_valid():
            return Response({"title": title, "header": header, "footer": footer,
                #Use the same form to display the errors
		"category_list": [{"title":"Unable to save","description":str(serializer.error_messages)}] })
        serializer.save()
        #Return to list state
        return redirect('list_categories')

class CategoryViewSet(viewsets.ModelViewSet):
    queryset = Categories.objects.order_by("name")
    serializer_class = CategorySerializer

"""
FAVORITES
"""

class FavoriteNew(generics.CreateAPIView):
    renderer_classes = [TemplateHTMLRenderer]
    template_name = "favorite/addFavorite.html"
    serializer_class = FavoriteSerializer

    def get(self, request, *args, **kwargs):
        form = FavoriteForm()
        return Response({"title": title, "header": header, "footer": footer,"form": form})

    def post(self,request,*args,**kwargs):
        data = request.data
        serializer = FavoriteSerializer(data=data)
            
        if not serializer.is_valid():
                #Use the same form to display the errors
            import pdb;pdb.set_trace()
            return Response({"title": title, "header": header, "footer": footer,
		"favorite_list": [{"title":"Unable to save","description":str(serializer.error_messages)}] })
        serializer.save()
        #show the list
        queryset = Favorites.objects.all()
        self.template_name = "favorite/favoriteList.html"
        return Response({"title": title, "header": header, "footer": footer,
                "favorite_list": queryset })

class FavoriteList(generics.ListCreateAPIView):
    renderer_classes = [TemplateHTMLRenderer]
    template_name = "favorite/favoriteList.html"
    serializer_class = FavoriteSerializer

    def get(self,request,*args,**kwargs):
        queryset = Favorites.objects.all()
        if (len(queryset) > 0):
            return Response({"title": title, "header": header, "footer": footer,
                "favorite_list": queryset})
        else:
            # redirect to form if empty
            self.template_name = "favorite/addFavorite.html"
            form = FavoriteForm()
            return Response({"title": title, "header": header, "footer": footer,"form": form})

    def post(self,request,*args,**kwargs):
        data = request.data
        serializer = FavoriteSerializer(data=data)
            
        if not serializer.is_valid():
                #Use the same form to display the errors
            import pdb;pdb.set_trace()
            return Response({"title": title, "header": header, "footer": footer,
		"favorite_list": [{"title":"Unable to save","description":str(serializer.error_messages)}] })
        serializer.save()
        #show the list
        queryset = Favorites.objects.all()
        self.template_name = "favorite/favoriteList.html"
        return Response({"title": title, "header": header, "footer": footer,
                "favorite_list": queryset })
class FavoriteDetail(generics.RetrieveUpdateDestroyAPIView):
    template_name = "favorite/favoriteDetail.html"
    serializer_class = FavoriteSerializer
    renderer_classes = [TemplateHTMLRenderer]

    #Read
    def get(self, request, pk):
        item = get_object_or_404(Favorites, pk=pk)
        form = FavoriteForm(instance=item)
        return Response({"title": title, "header": header, "footer": footer,
            "form": form})
    
    #update 
    def update(self,request,pk):
        item = get_object_or_404(Favorites, pk=pk)
        serializer = FavoriteSerializer(item, data=request.data)
        if not serializer.is_valid():
            return Response({"title": title, "header": header, "footer": footer,
                #Use the same form to display the errors
		"favorite_list": [{"title":"Unable to save","description":str(serializer.error_messages)}] })
        serializer.save()
        #Return to list state
        return redirect('list_favorites')

class FavoriteViewSet(viewsets.ModelViewSet):
    queryset = Favorites.objects.order_by("rank")
    serializer_class = FavoriteSerializer
