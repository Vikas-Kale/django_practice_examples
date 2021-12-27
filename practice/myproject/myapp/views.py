from django.shortcuts import render

# Create your views here.

def index(request):

    context = {"name": "Vikas"}

    return render(request, 'index.html',context)

def about(request):
    return render(request, 'about.html')