from django.shortcuts import render
from .forms import ContactForm
# Create your views here.

def contact(request):
    fm = ContactForm(initial={'name':'vikas'})
    fm.order_fields(field_order=['name','email','address','mobile_no'])
    return render(request, 'contact.html',{'form':fm})
