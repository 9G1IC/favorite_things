from django.db import models
from django_postgres_extensions.models.fields import HStoreField
from django.core.validators import MaxValueValidator

class Categories(models.Model):
    # Ensure the name is unique
    id = models.AutoField(primary_key=True)
    name = models.CharField(
        default="New Category",
        max_length=100,
        unique=True)

    def __str__(self):
        return self.name

    def as_json(self):
        return dict(name=self.name)

class Favorites(models.Model):
    id = models.AutoField(primary_key=True)
    title = models.CharField(max_length=100)
    description = models.TextField(blank=True)
    changeLog = models.CharField(blank=True,max_length=256)
    category = models.ForeignKey(
            Categories,null=True,on_delete=models.CASCADE)
    meta = HStoreField(blank=True,null=True)
    created_at = models.DateTimeField(auto_now=True)
    #Will be set on update
    modified_at = models.DateTimeField(auto_now=True)
    rank = models.PositiveIntegerField(default=0, validators=[MaxValueValidator(5)])

    def __str__(self):
        return "{}|{}".format(self.title,self.description)
    """
	Implementing quasi-blockchain instead of  GUID to detect change to the content
    """

    def compute_hash(self,*args,**kwargs):
        import hashlib
        string = str(kwargs)
        hash_object = hashlib.sha256(bytes(string,encoding="utf-8"))
        computed_hash = hash_object.hexdigest()
        kwargs['changeLog'] = computed_hash
        return kwargs

    def __init__(self, *args, **kwargs):
        kwargs = self.compute_hash(self, *args, **kwargs)
        super().__init__(*args, **kwargs)
        return
