from django.contrib import admin
from .models import *


# class SlidersAdmin(admin.ModelAdmin):
#     list_display = ('title_en', 'title_ar', 'status', 'image')
#     list_filter = ('status',)
#     search_fields = ('title_en', 'title_ar')
#     ordering = ('title_en',)
#     fieldsets = (
#         (None, {
#             'fields': ('title_en', 'title_ar', 'sub_title_en', 'sub_title_ar', 'image', 'status')
#         }),
#     )


# class AboutUsAdmin(admin.ModelAdmin):
#     list_display = ('title_en', 'title_ar', 'count_employee',
#                     'count_product', 'image')
#     search_fields = ('title_en', 'title_ar', 'content_en', 'content_ar')
#     ordering = ('title_en',)
#     fieldsets = (
#         (None, {
#             'fields': ('title_en', 'title_ar', 'content_en', 'content_ar', 'count_employee', 'count_product', 'image')
#         }),
#     )


# class ChooseUsAdmin(admin.ModelAdmin):
#     list_display = ('title_en', 'title_ar', 'image')
#     search_fields = ('title_en', 'title_ar', 'content_en', 'content_ar')
#     ordering = ('title_en',)
#     fieldsets = (
#         (None, {
#             'fields': ('title_en', 'title_ar', 'content_en', 'content_ar', 'image')
#         }),
#     )


# class ServiceAdmin(admin.ModelAdmin):
#     list_display = ('title_en', 'title_ar', 'status', 'image', 'icon_img')
#     list_filter = ('status',)
#     search_fields = ('title_en', 'title_ar')
#     ordering = ('title_en',)
#     fieldsets = (
#         (None, {
#             'fields': ('title_en', 'title_ar', 'content_en', 'content_ar', 'image', 'icon_img', 'status')
#         }),
#     )


# class SuggestionsAdmin(admin.ModelAdmin):
#     list_display = ('title_en', 'title_ar', 'status', 'icon_img')
#     list_filter = ('status',)
#     search_fields = ('title_en', 'title_ar')
#     ordering = ('title_en',)
#     fieldsets = (
#         (None, {
#             'fields': ('title_en', 'title_ar', 'content_en', 'content_ar', 'icon_img', 'status')
#         }),
#     )


# class CommentsAdmin(admin.ModelAdmin):
#     list_display = ('fullname_en', 'fullname_ar', 'status', 'image')
#     list_filter = ('status',)
#     search_fields = ('fullname_en', 'fullname_ar', 'content_en', 'content_ar')
#     ordering = ['fullname_en', 'fullname_ar']
#     fieldsets = (
#         (None, {
#             'fields': ('fullname_en', 'fullname_ar', 'content_en', 'content_ar', 'image', 'status')
#         }),
#     )


# class FAQAdmin(admin.ModelAdmin):
#     list_display = ('question_en', 'question_ar', 'status')
#     list_filter = ('status',)
#     search_fields = ('question_en', 'question_ar', 'answer_en', 'answer_ar')
#     fieldsets = (
#         (None, {
#             'fields': ('question_en', 'question_ar', 'answer_en', 'answer_ar','status')
#         }),
#     )


# admin.site.register(FAQ, FAQAdmin)
# admin.site.register(Sliders, SlidersAdmin)
# admin.site.register(AboutUs, AboutUsAdmin)
# admin.site.register(ChooseUs, ChooseUsAdmin)
# admin.site.register(Service, ServiceAdmin)
# admin.site.register(Suggestions, SuggestionsAdmin)
# admin.site.register(Comments, CommentsAdmin)

admin.site.register(SlidersEnglish)
admin.site.register(SlidersArabic)
admin.site.register(AboutUsEnglish)
admin.site.register(AboutUsArabic)
admin.site.register(ChooseUsEnglish)
admin.site.register(ChooseUsArabic)
admin.site.register(ServiceEnglish)
admin.site.register(ServiceArabic)
admin.site.register(CommentsEnglish)
admin.site.register(CommentsArabic)
admin.site.register(SuggestionsEnglish)
admin.site.register(SuggestionsArabic)
admin.site.register(FAQEnglish)
admin.site.register(FAQArabic)
