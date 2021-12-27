from django import forms 

class RegistrationForm(forms.Form):
    name = forms.CharField(max_length=50)
    email = forms.EmailField()
    password = forms.CharField(widget=forms.PasswordInput)

    