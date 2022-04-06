from socket import fromshare
from django import forms

from .models import Comment

class formComment(forms.ModelForm):
    
    class Meta:
        medel = Comment

        fields = ['comment', 'post']