from django.contrib import admin
from .models import *
# Register your models here.


class NewsAdmin(admin.ModelAdmin):
    list_display = ('title_en', 'title_ar', 'status', 'image')
    list_filter = ('status',)
    search_fields = ('title_en', 'title_ar', 'content_en', 'content_ar')
    ordering = ['title_en', 'title_ar']
    fieldsets = (
        (None, {
            'fields': ('title_en', 'title_ar', 'content_en', 'content_ar', 'image', 'status')
        }),
    )


admin.site.register(News, NewsAdmin)
