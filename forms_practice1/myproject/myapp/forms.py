from django import forms 

class ContactForm(forms.Form):
    name = forms.CharField()
    email = forms.EmailField()
    address = forms.CharField()
    department = forms.CharField()

    