from django import forms 

class StudentRegistration(forms.Form):
    name = forms.CharField(help_text="write your full name here")
    