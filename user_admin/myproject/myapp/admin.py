from django.contrib import admin
from django.contrib.admin.decorators import register

from .models import Students

# Register your models here.
@admin.register(Students)
class StudentAdmin(admin.ModelAdmin):
    list_display = ['stuid','stuname','stuemail','stuAddress']