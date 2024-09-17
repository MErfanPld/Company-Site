from django.contrib import admin
from .models import *


class SettingAdmin(admin.ModelAdmin):
    list_display = ('phone', 'email', 'address', 'logo')
    list_filter = ('phone',)
    search_fields = ('phone', 'email')
    ordering = ('phone',)
    fieldsets = (
        (None, {
            'fields': ('phone', 'email', 'address', 'logo')
        }),
    )

class SocialAdmin(admin.ModelAdmin):
    list_display = ('link', 'logo')
    search_fields = ('link',)
    ordering = ('link',)
    fieldsets = (
        (None, {
            'fields': ('link', 'logo')
        }),
    )

admin.site.register(Settings, SettingAdmin)
admin.site.register(Social, SocialAdmin)