from django.contrib import admin
from django.db.models import fields
from .models import Product


@admin.register(Product)
class ProductAdmin(admin.ModelAdmin):
    list_display = ('code', 'name', 'price',
                    'stock', 'unit', 'product_category')
    list_display_links = ('code', 'name')
    list_filter = ('code', 'name', 'product_category')
    list_per_page = 20

    search_fields = ('code', 'name', 'product_category')

    fieldsets = (
        (None, {
            'fields': (
                'code', 'name', 'description', 'price', 'stock', 'unit', 'product_category'
            ),
        }),
    )
