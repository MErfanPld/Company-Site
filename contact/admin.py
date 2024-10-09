from django.contrib import admin
from .models import *

# Register your models here.

class ContactUsAdmin(admin.ModelAdmin):
    list_display = ('fullname', 'email', 'phone','status')
    list_filter = ('status',)
    search_fields = ('fullname', 'email', 'phone')


admin.site.register(ContactUs, ContactUsAdmin)