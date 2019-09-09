from django.forms import ModelForm
from favorite_things_app.models import *

class FavoriteForm(ModelForm):
    class Meta:
        model = Favorites
        exclude = ["changeLog","created_at","modified_at"]
        can_order = True
        can_delete = True
        fields = "__all__"

