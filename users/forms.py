from django import forms
from .models import Profile

class ProfileUpdateForm(forms.ModelForm):
    bio = forms.CharField(widget=forms.Textarea(attrs={'rows': 2}))
    class Meta:
        model = Profile
        fields = ['name','bio','avatar']
