from django.contrib import admin
from django.contrib.admin import ModelAdmin

from metall.models import Product, Category


@admin.register(Category)
class CategoryAdmin(ModelAdmin):
    list_display = ('title', 'slug')
    prepopulated_fields = {'slug': ('title',)}


@admin.register(Product)
class ProductAdmin(ModelAdmin):
    list_display = ('name', 'size', 'clen', 'nton', 'price', 'is_active', 'is_discount')
