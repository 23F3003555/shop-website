from django.contrib import admin
from .models import Product


@admin.register(Product)
class ProductAdmin(admin.ModelAdmin):

    list_display = (
        "name",
        "category",
        "subcategory",
        "brand",
        "model",
        "size",
        "price",
        "available",
    )

    list_filter = (
        "category",
        "subcategory",
        "available",
    )

    search_fields = (
        "name",
        "brand",
        "model",
        "size",
    )

    list_editable = (
        "available",
    )

    ordering = (
        "-created_at",
    )