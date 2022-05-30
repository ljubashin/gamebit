from django import forms
from .models import Review

class Reviewform(forms.ModelForm):
    class Meta:
        model = Review
        exclude = ["game"]
        label = {
            "user_name": "Your Name",
            "text": "Your Comment",
            "like": "Do you like this game",
            "dislike": "Do you dislike this game"
        }
        widgets = {
            "user_name" : forms.TextInput(attrs={'class': "form__field"}),
            "text" : forms.TextInput(attrs={'class': "form__field"}),
            "like" : forms.CheckboxInput(attrs={'class': "boolean"}),
            "dislike" : forms.CheckboxInput(attrs={'class': "noboolean"}),
        }