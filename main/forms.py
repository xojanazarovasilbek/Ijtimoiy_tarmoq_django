from django import forms
from .models import Post

class PostForm(forms.ModelForm):
    class Meta:
        model = Post
        fields = ['body', 'media']
        widgets = {
            'body': forms.Textarea(attrs={'rows':4, 'class':'form-control', 'placeholder':"What's on your mind?"}),
        }