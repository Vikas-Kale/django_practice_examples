from django.shortcuts import render

# Create your views here.

from myapp.models import Student

def studentinfo(request):
    stud = Student.objects.all()
    return render(request, 'myapp/studetails.html',{"stu":stud})

def pickone_data(request):
    stud = Student.objects.get(pk = 1)

    return render(request, 'myapp/onedata.html',{"stu":stud})