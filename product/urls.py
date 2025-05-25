from django.urls import path
from .views import *
urlpatterns = [
    path('products/', get_products, name='products-list'),
    path('products/<int:pk>/', get_product, name='product-detail'),
]
