from django.contrib import admin
from .models import Category, Product

@admin.register(Category)
class CategoryAdmin(admin.ModelAdmin):
    list_display = ['name', 'slug']
    prepopulated_fields = {'slug': ('name',)}

@admin.register(Product)
class ProductAdmin(admin.ModelAdmin):
    list_display = ['article', 'name', 'slug', 'shelf_life', 'halal', 'ean_13']
    list_filter = ['article', 'created', 'updated']
    prepopulated_fields = {'slug': ('name',)}
