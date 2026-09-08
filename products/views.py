from django.shortcuts import render, get_object_or_404
from .models import Product


def product_list(request):

    products = Product.objects.filter(
        available=True
    )

    category = request.GET.get("category")
    search = request.GET.get("search")

    if category:
        products = products.filter(
            category=category
        )

    if search:
        products = products.filter(
            name__icontains=search
        ) | products.filter(
            brand__icontains=search
        ) | products.filter(
            model__icontains=search
        ) | products.filter(
            subcategory__icontains=search
        )

    categories = Product.CATEGORY_CHOICES

    context = {
        "products": products,
        "categories": categories,
        "selected_category": category,
        "search": search or "",
    }

    return render(
        request,
        "products/product_list.html",
        context
    )


def product_detail(request, id):

    product = get_object_or_404(
        Product,
        id=id,
        available=True
    )

    return render(
        request,
        "products/product_detail.html",
        {
            "product": product
        }
    )