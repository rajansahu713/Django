from django.shortcuts import render
from fn_api.models import Product
from fn_api.serializers import ProductSerializer
from rest_framework.generics import RetrieveUpdateDestroyAPIView
# Create your views here.

class ProductList(RetrieveUpdateDestroyAPIView):
    queryset = Product.objects.all()
    serializer_class = ProductSerializer