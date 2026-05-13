from django.contrib import admin
from .models import Category, MenuItem


@admin.register(Category)
class CategoryAdmin(admin.ModelAdmin):
    list_display = ['name', 'icon', 'priority_order']
    list_editable = ['priority_order', 'icon']
    search_fields = ['name']
    list_filter = ['priority_order']


@admin.register(MenuItem)
class MenuItemAdmin(admin.ModelAdmin):
    list_display = ('name', 'price', 'category'
                    , 'is_available', 'is_featured', 'priority_order')
    list_filter = ['category', 'is_available', 'is_featured']
    list_editable = ['price', 'is_available', 'is_featured', 'priority_order']
    search_fields = ['name', 'description']

    raw_id_fields = ['category']
