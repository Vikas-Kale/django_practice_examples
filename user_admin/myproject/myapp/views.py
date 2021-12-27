from django.shortcuts import render
from .forms import StudentRegistration

# Create your views here.

def home(request):
    

    return render(request,"home.html",{'myname':'Vikas'})

def about(request):
    return render(request, "about.html")

def contact(requset):
    return render(requset, "contact.html")

def showformdata(request):
    fm = StudentRegistration()
    return render(request,'contact.html',{"form":fm})