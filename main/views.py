from django.shortcuts import render

# Create your views here.
from main.models import Category, Product, Brand


def home(request):
    return render(request,'index.html')


def category_list(request):
    data = Category.objects.all().order_by('-id')
    return render(request, 'category_list.html', {'data': data})



# brand
def brand_list(request):
    data = Brand.objects.all().order_by('-id')
    return render(request, 'brand_list.html', {'data': data})


# product list
def product_list(request):
    data = Product.objects.all().order_by('-id')
    return render(request, 'product_list.html', {'data': data})