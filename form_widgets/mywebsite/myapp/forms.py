from django import forms 

class StudentForm(forms.Form):
    name = forms.CharField(max_length=50,widget=forms.FileInput)
    email = forms.EmailField()
    mobile = forms.IntegerField()
