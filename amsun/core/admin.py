from django.contrib import admin
from .models import Events, News, Blog

# Register your models here.

@admin.register(Events)
class EventsAdmin(admin.ModelAdmin):
    list_display = ('title', 'date', 'category', 'location')
    list_filter = ('category', 'date')
    search_fields = ('title', 'description')

@admin.register(News)
class NewsAdmin(admin.ModelAdmin):
    list_display = ('headline', 'published_date', 'category', 'author')
    list_filter = ('category', 'published_date')
    search_fields = ('headline', 'content')

@admin.register(Blog)
class BlogAdmin(admin.ModelAdmin):
    list_display = ('title', 'author', 'created_at', 'category')
    list_filter = ('category', 'created_at')
    search_fields = ('title', 'body', 'author')
