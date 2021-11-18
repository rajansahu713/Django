from fn_api.models import Product
from rest_framework.views import APIView
from rest_framework.response import Response
from fn_api.serializers import ProductSerializer
# Create your views here.

class ProductList(APIView):
    def get(self,request):
        id = request.query_params.get('id')
        if id is not None:
            product = Product.objects.get(product_id=id)
            serializer = ProductSerializer(product)
            return Response(serializer.data)
        products = Product.objects.all()
        serializer = ProductSerializer(products, many=True)
        return Response(serializer.data)

    def post(self,request):
        serializer = ProductSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors)
    
    def put(self,request):
        id = request.query_params.get('id')
        product = Product.objects.get(product_id=id)
        serializer = ProductSerializer(product, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=400)
        
    def delete(self,request):
        id = request.query_params.get('id')
        product = Product.objects.get(product_id=id)
        product.delete()
        return Response(status=204)
        
    def patch(self,request):
        id = request.query_params.get('id')
        product = Product.objects.get(product_id=id)
        serializer = ProductSerializer(product, data=request.data, partial=True)    
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=400)
    

