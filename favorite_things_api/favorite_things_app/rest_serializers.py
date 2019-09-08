from rest_framework import serializers
from drf_writable_nested import WritableNestedModelSerializer
from favorite_things_app.models import *

class CategorySerializer(serializers.ModelSerializer):
    class Meta:
        model = Categories
        fields = '__all__'

class FavoriteSerializer(serializers.ModelSerializer):
    category = serializers.SlugRelatedField(slug_field="id",queryset=Categories.objects.all(),required=True)
        
    class Meta:
        model = Favorites
        fields = '__all__'

    def create(self, data,*args,**kwargs):
        #get all instances of records in the category of data
        if 'category' in data:
            all_records_with_input_category = Favorites.objects.get(category=data['category'])
        return data

        # TODO:include category
        instance.save()
        return instance

    def update(self, instance, data):
        # Recalculate hash
        import hashlib
        from datetime import datetime
        string = str(data)
        hash_object = hashlib.sha256(bytes(string, encoding="utf-8"))
        computedHash = hash_object.hexdigest()
        data["changeLog"] = computedHash
        data["modified_at"] = datetime.now()
        instance.changeLog = data.get('changeLog', instance.changeLog)
        instance.description = data.get('description', instance.description)
        instance.modified_at = data.get('modified_at', instance.modified_at)
        instance.title = data.get('title', instance.title)
        # TODO:include category
        instance.save()
        return instance
