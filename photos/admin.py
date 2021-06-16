from django.contrib import admin
from photos.models import Photos, Category


class CategoryAdmin(admin.ModelAdmin):
    list_display = ['name']
    search_fields = ['name']


class PhotosAdmin(admin.ModelAdmin):
    list_display = ['title', 'category']
    search_fields = ['name']
    autocomplete_fields = ['category']


admin.site.register(Category, CategoryAdmin)
admin.site.register(Photos, PhotosAdmin)
