from django.shortcuts import render
from .forms import ContactForm
# Create your views here.

def contact(request):
    fm = ContactForm()
    return render(request, "contact.html",{'form':fm})
    