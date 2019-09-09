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


class FavoriteNew(generics.CreateAPIView):
    template_name = "favorite/addFavorite.html"
    serializer_class = FavoriteSerializer
    renderer_classes = [TemplateHTMLRenderer]

    def get(self,request,*args,**kwargs):
        form = FavoriteForm()
        return Response({"title": title, "header": header, "footer": footer,"form": form})

    def create(self,request,*args,**kwargs):
        data = request.data
        serializer = FavoriteSerializer(data=data)
        if not serializer.is_valid():
            return Response({"title": title, "header": header, "footer": footer,
		"favorite_list": [{"title":"Unable to save","description":str(serializer.error_messages)}] })
        serializer.save()
        queryset = Favorites.objects.all()
        #show the list
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
    def put(self,*args,**kwargs):
        item = get_object_or_404(Favorites, pk=pk)
        serializer = FavoriteSerializer(item, data=request.data)
        if not serializer.is_valid():
            return Response({'serializer': serializer, 'item': item})
        serializer.save()
        #Return to list state
        return redirect('list_favorites')

class FavoriteViewSet(viewsets.ModelViewSet):
    queryset = Favorites.objects.order_by("rank")
    serializer_class = FavoriteSerializer
