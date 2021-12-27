from django.urls import path
from .views import home,about,contact,showformdata

urlpatterns = [
    path('',home,name="home"),
    path('about',about,name="about"),
    path('contact',contact,name="contact"),
    path('showformdata',showformdata,name="showformdata"),
]
