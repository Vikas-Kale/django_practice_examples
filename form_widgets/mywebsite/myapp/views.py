from django.shortcuts import render
from .forms import StudentForm
# Create your views here.

def contact_form(request):
    fm = StudentForm()
    return render(request, 'contact.html',{'form':fm})

