from django.shortcuts import render
from .forms import StudentRegistration
# Create your views here.

def home(request):
    fm = StudentRegistration()
    return render(request, 'home.html',{'form':fm})