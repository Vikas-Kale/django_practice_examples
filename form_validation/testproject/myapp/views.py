from django.shortcuts import render
from .forms import RegistrtionForm
# Create your views here.

def home(request):
    if request.method == "POST":
        fm = RegistrtionForm(request.POST)
        if fm.is_valid():
            print('form validated')
            name = fm.cleaned_data['name']
            email = fm.cleaned_data['email']
            mobile_number = fm.cleaned_data['mobile_number']
            password = fm.cleaned_data['password']
            print(name)
            print(email)
            print(mobile_number)
            print(password)
            fm = RegistrtionForm()

    else:
        fm = RegistrtionForm()
        
    return render(request, 'home.html', {'form':fm})
