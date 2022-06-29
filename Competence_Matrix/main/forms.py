from .models import Model, KSP, modelList
from django.forms import ModelForm, Textarea, TextInput

class ModelForm(ModelForm):
    class Meta:
        model = Model
        fields = ["name", "description"]
        widgets = {
            "name": 
        }