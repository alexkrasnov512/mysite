from django.contrib import admin
from .models import *

# Register your models here.


class ArticleAdmin(admin.ModelAdmin):
    list_display = ('id', 'author', 'title', 'time_create', 'image', 'time_update')
    list_display_links = ('id', 'title')
    search_fields = ('title', 'body')
    list_filter = ('title',)
    prepopulated_fields = {"slug": ("title",)}

admin.site.register(Article, ArticleAdmin)