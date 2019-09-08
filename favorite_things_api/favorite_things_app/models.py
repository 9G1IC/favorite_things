from django.db import models
from django_postgres_extensions.models.fields import HStoreField
from django.core.validators import MaxValueValidator

# Create your models here.

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
    changeLog = models.CharField(blank=True,max)
    category = models.ForeignKey(
            Categories,null=True,on_delete=models.CASCADE)
    meta = HStoreField(blank=True,on_delete=models.CASCADE)
    created_at = models.DateTimeField(auto_now=True)
    #Will be set on update
    modified_at = models.DateTimeField(auto_now=True)
    rank = models.PositiveIntegerField(
            default=0, validators[MaxValueValidator(5)])

    def __str__(self):
        return "{}|{}".format(self.title,self.description)
