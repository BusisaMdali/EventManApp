from django import forms
from .models import Event

class EventForm(forms.ModelForm):
    class Meta:
        model = Event
        fields = ['title' , 'description' , 'date' , 'time' , 'endTime' , 'image', 'location']
        widgets = {
            'title' : forms.TextInput(attrs={'class':'form-control'}),
            'description' : forms.Textarea(attrs={'class':'form-control'}),
            'date' : forms.DateInput(attrs={'class':'form-control','type':'date'}),
            'time' : forms.DateInput(attrs={'class':'form-control','type':'time'}),
            'endTime' : forms.DateInput(attrs={'class': 'form-control','type': 'time'}),
            'image' : forms.ClearableFileInput(attrs={'class':'form-control'}),
            'location' : forms.TextInput(attrs={'class':'form-control'}),
        }