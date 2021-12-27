from django import forms 

class StudentRegistration(forms.Form):
    name = forms.CharField()
    email = forms.EmailField(initial='kalevikas145@gmail.com', disabled='True',help_text="Enter personal email id")
    mobile = forms.IntegerField()