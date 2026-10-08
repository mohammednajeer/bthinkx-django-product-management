from django.shortcuts import render
from django.contrib.auth.decorators import login_required
from django.core.paginator import Paginator

from .models import Product, Category


@login_required
def dashboard(request):
    total_products = Product.objects.count()

    active_products = Product.objects.filter(
        status='active'
    ).count()

    inactive_products = Product.objects.filter(
        status='inactive'
    ).count()

    low_stock_products = Product.objects.filter(
        stock__lte=5
    ).count()

    context = {
        'total_products': total_products,
        'active_products': active_products,
        'inactive_products': inactive_products,
        'low_stock_products': low_stock_products,
    }

    return render(request, 'products/dashboard.html', context)

@login_required
def product_list(request):
    products = Product.objects.all().order_by('-created_at')
    categories = Category.objects.all()
    search = request.GET.get('search', '')
    paginator = Paginator(products, 10)

    page_number = request.GET.get('page')
    page_obj = paginator.get_page(page_number)
    

    if search:
        products = products.filter(name__icontains=search)

    context = {
        'products': page_obj,
        'categories': categories,
        'search': search,
    }

    return render(request, 'products/product_list.html', context)