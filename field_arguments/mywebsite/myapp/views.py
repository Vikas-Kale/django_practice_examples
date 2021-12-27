from django.shortcuts import render
from .forms import StudentRegistration
# Create your views here.

def contact(request):
    fm = StudentRegistration()
    return render(request,'contact.html',{'form':fm})
