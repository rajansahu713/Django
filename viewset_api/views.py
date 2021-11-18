from django.shortcuts import get_object_or_404
from rest_framework import viewsets
from rest_framework.response import Response
from fn_api.models import Product
from fn_api.serializers import ProductSerializer

# Create your views here.

class ProductViewSet(viewsets.ViewSet):
    def list(self,request):
        queryset = Product.objects.all()
        serializer = ProductSerializer(queryset,many=True)
        return Response(serializer.data)
    
    def create(self,request):
        serializer = ProductSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors)
    
    def retrieve(self,request,pk=None):
        queryset = Product.objects.all()
        product = get_object_or_404(queryset,pk=pk)
        serializer = ProductSerializer(product)
        return Response(serializer.data)
    
    def update(self,request,pk=None):   
        product = Product.objects.get(pk=pk)
        serializer = ProductSerializer(product,data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors)
    
    def destroy(self,request,pk=None):
        product = Product.objects.get(pk=pk)
        product.delete()
        return Response('Item deleted')

    