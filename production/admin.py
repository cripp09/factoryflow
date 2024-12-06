import csv
import io
from django.contrib import admin
from django.urls import path
from django.shortcuts import render
from django.http import HttpResponse
from .models import Category, Product


"""Функция импорта из CSV"""
def import_from_csv(modeladmin, request, queryset):
    pass
import_from_csv.short_description = "Импортировать данные из CSV"


@admin.register(Category)
class CategoryAdmin(admin.ModelAdmin):
    list_display = ['name', 'slug']
    prepopulated_fields = {'slug': ('name',)}
    actions = [import_from_csv]


@admin.register(Product)
class ProductAdmin(admin.ModelAdmin):
    list_display = ['article', 'name', 'shelf_life', 'halal', 'ean_13']
    list_filter = ['article', 'created', 'updated']
    prepopulated_fields = {'slug': ('name',)}
    actions = [import_from_csv]
