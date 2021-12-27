from django.shortcuts import render

# Create your views here.

from .forms import StudentRegistration

def showformdata(request):
    fm = StudentRegistration()
    return render(request, 'userregistration.html',{'form':fm})
    