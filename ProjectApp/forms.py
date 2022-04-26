from django import forms
from django import forms
from .models import Projects , Users


class Projects(forms.ModelForm):
    class Meta:
        model =  Projects
        fields = '__all__'



class Users(forms.ModelForm):
    class Meta:
        model =  Users
        fields = '__all__'



