from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.


def index(request):
    return render(request, 'index.html', {'name':'Vikas'})

def about(request):
    return render(request, 'about.html', {'course':'Python'})

def contact(request):
    return render(request, 'contact.html',{'number':'7798743804'})

