from django.shortcuts import render
from django.http import HttpResponse
from .models import Product, Store, Category

def home(request):
    products = Product.objects.all()
    best_selling_products = products
    products = products[:8]
    categories = Category.objects.all()[:4]
    stores= Store.objects.all()[:4]

    context={
        'products':products,
        'categories':categories,
        'stores':stores,
        'best_selling_products':best_selling_products
    }

    return render(request, 'core/home.html', context)

def products(request):
    products = Product.objects.all()
    categories = Category.objects.all()
    context = {'products':products, 'categories':categories}
    return render(request, 'core/products.html', context)

def product(request, id):
    product = Product.objects.get(id=id)
    related_products = Product.objects.filter(category=product.category).exclude(id=product.id)
    return render(request, 'core/detail.html', {'product':product, 'related_products':related_products})
   
def stores(request):
    stores = Store.objects.all()
    
def store(request, id):
    pass

def store_products(request, id):
    pass

def categories(request):
    pass

def category(request, id):
    pass