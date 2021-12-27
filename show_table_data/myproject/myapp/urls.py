from django.urls import path
from . import views

urlpatterns = [
    path('info/', views.studentinfo, name='info'),
    path('pick/', views.pickone_data, name='pick')
]
