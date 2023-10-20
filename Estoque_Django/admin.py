# from django.contrib import admin
# from .models import Products

# class ProductsAdmin(admin.ModelAdmin):

#     list_display = ['nome','price', 'size', 'in_stock']
#     list_filter = ['in_stock']
#     list_editable = ['size']
#     search_fields = ['nome']

# admin.site.register(Products, ProductsAdmin)


from django.contrib import admin
from .models import Products, Categories


class ProductsAdmin(admin.ModelAdmin):
    list_display = ['name', 'price', 'in_stock']
    list_filter = ['in_stock']
    search_fields = ['name']


admin.site.register(Products, ProductsAdmin)

admin.site.register(Categories)


