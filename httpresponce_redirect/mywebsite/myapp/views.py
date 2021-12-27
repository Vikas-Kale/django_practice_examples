from django.shortcuts import render
from .forms import RegistrationForm
# Create your views here.

def home(request):
    if request.method == 'POST':
        fm = RegistrationForm(request.POST)
        if fm.is_valid():
            name = fm.cleaned_data['name']
            email = fm.cleaned_data['email']
            password = fm.cleaned_data['password']
            print(name)
            print(email)
            print(password)
            return render(request, 'success.html', {'form': fm})
    else:
        fm = RegistrationForm()
    
    return render(request, 'home.html', {'form': fm})