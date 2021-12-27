from django import forms 

class ContactForm(forms.Form):
    name = forms.CharField()
    email = forms.EmailField()
    mobile_no = forms.IntegerField()
    address = forms.CharField()

