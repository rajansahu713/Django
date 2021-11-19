from django.shortcuts import render
from fn_api.models import Product
from fn_api.serializers import ProductSerializer
from rest_framework.viewsets import ModelViewSet
# Create your views here.

class ProductViewSet(ModelViewSet):
    queryset = Product.objects.all()
    serializer_class = ProductSerializer
