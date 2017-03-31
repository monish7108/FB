from django import forms
from .models import *

class CreatePostForm(forms.ModelForm):

    class Meta:
        model = PostsByUser
        fields = '__all__'