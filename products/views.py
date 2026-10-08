from django.shortcuts import render,redirect
from django.contrib.auth.decorators import login_required
from django.core.paginator import Paginator
from .forms import ProductForm
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
    search = request.GET.get('search', '')
    category_id = request.GET.get('category', '')
    status = request.GET.get('status', '')
    products = Product.objects.all()

    if search:
        products = products.filter(name__icontains=search)

    if category_id:
        products = products.filter(category_id=category_id)

    if status:
        products = products.filter(status=status)

    products = products.order_by('-created_at')
    categories = Category.objects.all()
    paginator = Paginator(products, 10)
    page_number = request.GET.get('page')
    page_obj = paginator.get_page(page_number)

    context = {
        'products': page_obj,
        'categories': categories,
    }

    return render(request, 'products/product_list.html', context)

@login_required
def product_create(request):

    if request.method == 'POST':
        form = ProductForm(request.POST, request.FILES)

        if form.is_valid():
            form.save()
            return redirect('product_list')

    else:
        form = ProductForm()

    return render(
        request,
        'products/product_form.html',
        {'form': form}
    )