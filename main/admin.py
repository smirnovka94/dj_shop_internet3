from django.contrib import admin

from main.models import Category, Product, Version


@admin.register(Category)
class CategoryAdmin(admin.ModelAdmin):
    list_display = ('pk', 'name',)
    list_filter = ('name',)
    search_fields = ('name', 'description',)


@admin.register(Product)
class ProductAdmin(admin.ModelAdmin):
    list_display = ('pk', 'name', 'cost', 'category')
    list_filter = ('category',)
    search_fields = ('name', 'description',)

@admin.register(Version)
class ProductAdmin(admin.ModelAdmin):
    list_display = ('version_number', 'version_name', 'product')
    list_filter = ('is_active',)
