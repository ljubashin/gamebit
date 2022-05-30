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
        