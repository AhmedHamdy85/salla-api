from django.shortcuts import render
from rest_framework.decorators import api_view
from .models import Product
from rest_framework.response import Response
from .serializers import ProductSerializer
@api_view(['GET'])
def get_products(request):
    products = Product.objects.all()
    serializer = ProductSerializer(products,many=True,context={'request':request})
    return Response({'data': serializer.data})