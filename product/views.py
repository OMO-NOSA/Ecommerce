from django.shortcuts import render
from django.views import ListView
from . models import product

class ProductList(ListView):
    queryset = Product.objects.all()

    