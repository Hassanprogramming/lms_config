from django import forms
from .models import *

class AddcontactForm(forms.ModelForm):
    class Meta:
        model = ContactUs
        fields = [
            "name",
            "email",
            "message",
        ]
        

class AddCommentForm(forms.ModelForm):
    class Meta:
        model = Comment
        fields = [
            "user_name",
            "email",
            "text",
        ]