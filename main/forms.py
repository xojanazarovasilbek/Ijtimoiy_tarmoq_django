from django import forms
from .models import Post,Comment

class PostForm(forms.ModelForm):
    class Meta:
        model = Post
        fields = ['body', 'media']
        widgets = {
            'body': forms.Textarea(attrs={'rows':4, 'class':'form-control', 'placeholder':"What's on your mind?"}),
        }


class CommentForm(forms.ModelForm):
    class Meta:
        model = Comment
        fields = ["body"]
        widgets = {
            "body": forms.Textarea(attrs={"rows": 2, "placeholder": "Write a comment..."}),
        }