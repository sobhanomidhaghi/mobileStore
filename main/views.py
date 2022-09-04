from django.shortcuts import render

# Create your views here.
from main.models import Category


def home(request):
    return render(request,'index.html')


def category_list(request):
    data = Category.objects.all().order_by('-id')
    return render(request, 'category_list.html', {'data': data})
