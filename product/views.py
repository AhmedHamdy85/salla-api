from django.shortcuts import render
from rest_framework.decorators import api_view
from .models import Product
from rest_framework.response import Response
from .serializers import ProductSerializer
from .filtters import ProductFilter
from rest_framework.pagination import PageNumberPagination
@api_view(['GET'])
def get_products(request):
    filterset=ProductFilter(request.GET,queryset=Product.objects.all().order_by('id'))
    resPage=2
    paginator=PageNumberPagination()
    paginator.page_size=resPage
    queryset=paginator.paginate_queryset(filterset.qs,request)

    serializer = ProductSerializer(queryset,many=True,context={'request':request})
    return paginator.get_paginated_response(
       
            
            serializer.data
      
    ) 

@api_view(['GET'])
def get_product(request,pk):
    product=Product.objects.get(pk=pk)
    serializer= ProductSerializer(product,context={'request':request})
    return Response(
        {
            "product":serializer.data
        }
    )

