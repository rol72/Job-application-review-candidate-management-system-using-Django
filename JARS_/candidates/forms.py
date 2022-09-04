from django import forms 
from .models import Candidate



class CandidateForm(forms.ModelForm):
  class Meta:
    model = Candidate
    fields = ['projects', 'skillmat', 'name', 'email', 'field_of_study', 'exp','skills','projectss']
    labels = {
      'projects': 'projects', 
      'skillmat': 'Do you know Django?', 
      'name': 'Name', 
      'email': 'Email', 
      'field_of_study': 'Field of Study', 
      'exp': 'exp',
      'skills':'skills',
      'projectss':'Title of projects',
      

    }
    widgets = {
      'projects': forms.NumberInput(attrs={'class': 'form-control'}), 
      'skillmat': forms.TextInput(attrs={'class': 'form-control'}),
      'name': forms.TextInput(attrs={'class': 'form-control'}),
      'email': forms.EmailInput(attrs={'class': 'form-control'}),
      'field_of_study': forms.TextInput(attrs={'class': 'form-control'}),
      'exp': forms.NumberInput(attrs={'class': 'form-control'}),
      'skills':forms.TextInput(attrs={'class': 'form-control'}),
      'projectss':forms.TextInput(attrs={'class': 'form-control'}),
    }