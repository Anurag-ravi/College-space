from django import forms
from .models import Post

class PostForm(forms.ModelForm):
    content = forms.CharField(widget=forms.Textarea(attrs={'rows': 2}))
    class Meta:
        model = Post
        fields = ['content','image',]