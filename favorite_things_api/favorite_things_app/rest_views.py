from rest_framework import generics, viewsets
from rest_framework.renderers import TemplateHTMLRenderer
from rest_framework.response import Response
from django.shortcuts import get_object_or_404, redirect
from django.forms import modelformset_factory

# Import local modules
from favorite_things_app.models import *
from favorite_things_app.rest_serializers import *

class FavoriteNew(generics.CreateAPIView):
    template_name = "favorite/addFavorite.html"
    serializer_class = FavoriteSerializer
    renderer_classes = [TemplateHTMLRenderer]

    def get(self,request,*args,**kwargs):
        import pdb;pdb.set_trace()
        form = FavoriteForm()
        return Response({"title": title, "header": header, "footer": footer,"form": form})

class FavoriteDetail(generics.RetrieveUpdateDestroyAPIView):
    template_name = "favorite/favoriteDetail.html"
    serializer_class = FavoriteSerializer
    renderer_classes = [TemplateHTMLRenderer]

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
