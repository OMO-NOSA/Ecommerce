from django.urls import path
from product.views import (ProductListView,
                            ProductDetailView,
                            ProductFeatureListView,
                            ProductFeatureDetailView,)


urlpatterns = [
    path('', ProductListView.as_view(), name='product_list'),
    path('<int:pk>/', ProductDetailView.as_view(), name='product_detail'),
    path('featured',ProductFeatureListView.as_view(), name='featured'),
    path('<int:pk>/', ProductFeatureDetailView.as_view(), name='featured_detail')
]
