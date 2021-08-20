from django import forms
from .models import Quiz,Assignment

class QuizForm(forms.ModelForm):
    class Meta:
        model = Quiz
        fields = ['title', 'course', 'description', 'date', 'time_from', 'time_to']
        widgets = {
            'date': forms.DateInput(attrs={'class':'form-control', 'type':'date'}),
            'time_from': forms.TimeInput(attrs={'class':'form-control', 'type':'time'}),
            'time_to': forms.TimeInput(attrs={'class':'form-control', 'type':'time'}),
        }

class AssignmentForm(forms.ModelForm):
    class Meta:
        model = Assignment
        fields = ['title', 'course', 'description', 'deadline', 'time']
        widgets = {
            'deadline': forms.DateInput(attrs={'class':'form-control', 'type':'date'}),
            'time': forms.TimeInput(attrs={'class':'form-control', 'type':'time'}),
        }