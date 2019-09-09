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
    """
    Pass the filtered records, and output the value of data
    """
    def process_reorder(self,filtered_records,data):
        #Do not compare records with themselves
            filter_length = len(filtered_records)
            if(filter_length > 1):
                #Since the titles must be unique, we can identify a record uniquely by the title
                #List comprehension does not seem to be effective, because, we need to count the iterations
                for i in range(0,filter_length):
                    record = filtered_records[i] 
                    if record.rank == data['rank'] and record.title != data['title'] and i < filter_length - 1:
                        self.reorder(record,data) 

            return data
    #Main reordering engine
    def reorder(self,record,data):
        if record.rank == data['rank']:
            #This is assuming the lower the rank, the higher the priority
            record.rank = record.rank + 1
            record.save()
            self.reorder(record,data)
        return record

    def create(self, data,*args,**kwargs):
        #get all instances of records in the category of data
        if 'category' in data:
            filtered_records = Favorites.objects.filter(category=data['category'])
            data = self.process_reorder(filtered_records,data)
        return data

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
