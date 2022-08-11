
1. Create Django Form from Models

Django ModelForm is a class that is used to directly convert a model into a Django form.
If you’re building a database-driven app, 
chances are you’ll have forms that map closely to Django models.

# import form class from django
from django import forms
  
# import GeeksModel from models.py
from .models import GeeksModel
  
# create a ModelForm
class GeeksForm(forms.ModelForm):
    # specify the name of model to use
    class Meta:
        model = GeeksModel
        fields = "__all__"

