from django.shortcuts import render
from django.http import Http404
from django.views.generic import ListView,DetailView
from . models import Product

class ProductFeatureListView(ListView):
    template_name = "product/list.html"

    def get_queryset(SELF,*args, **kwargs):
        request = self.request
        return Product.objects.featured()

class ProductFeatureDetailView(DetailView):
    queryset = Product.objects.featured()
    template_name = "product/featured_detail.html"
class ProductListView(ListView):
    queryset = Product.objects.all()
    template_name = "product/list.html"

    # def get_context_data(self, *args, **kwargs):
    #     context = super(ProductListView,self).get_context_data(*args, **kwargs)
    #     return context
class ProductDetailView(DetailView):
    queryset = Product.objects.all()
    template_name = "product/detail.html"

    def get_context_data(self, *args, **kwargs):
        context = super(ProductDetailView,self).get_context_data(*args, **kwargs)
        return context

    def get_object(self, *args, **kwargs):
        request = self.request
        pk = self.kwargs.get('pk')
        instance = Product.objects.get_by_id(pk)
        if instance is None:
            raise Http404("Product doesn't exist")
        return instance