from django.contrib import admin
from .forms import ContactForm

from .models import Contact
# Register your models here.
@admin.register(Contact)
class ContactAdmin(admin.ModelAdmin):
    list_display = ["name","email","address","department"]