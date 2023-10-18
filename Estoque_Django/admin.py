from django.contrib import admin
from .models import Products

class ProductsAdmin(admin.ModelAdmin):

    list_display = ['nome','price', 'size', 'in_stock']
    list_filter = ['in_stock']
    list_editable = ['size']
    search_fields = ['nome']

admin.site.register(Products, ProductsAdmin)