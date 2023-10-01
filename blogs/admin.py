from django.contrib import admin

from blogs.models import Blog


@admin.register(Blog)
class BlogsAdmin(admin.ModelAdmin):
    list_display = ('pk', 'title',)
    list_filter = ('title',)
    search_fields = ('title', 'content',)