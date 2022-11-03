from django import forms
from myApp.models import Post, Comment

class PostForm(forms.ModelForm):
    
    class Meta:
        model = Post
        fields = ("title", "text_info", "text", "yazar", "image")


class CommentForm(forms.ModelForm):
    """Form definition for Comment."""

    class Meta:
        """Meta definition for Commentform."""

        model = Comment
        fields = ('name','text')
