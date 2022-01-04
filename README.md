# Django

In this repo i have perform CRUD operation in multiple ways
1. Funtion base view
2. Apiview
3. Generic Apiview
4. Viewset
5. ModelViewset
6. Concrete Apiview

I have created a project **app** by using 
```python
django-admin startproject app
```

After that i have created multiples app by using 
```python
python manage.py startapp fun_api
```
Simillarly, created others app 

Create a models and serializer in fun_api **app** and used in others app by importing it

models
```python
from django.db import models

# Create your models here.
class Product(models.Model):
    product_id = models.AutoField(primary_key=True)
    product_name = models.CharField(max_length=50)
    category = models.CharField(max_length=50, default="") 

    def __str__(self):
        return self.product_name
```

Serializers
```python
from rest_framework import serializers
from .models import Product

class ProductSerializer(serializers.ModelSerializer):
    class Meta:
        model = Product
        fields = ('product_id', 'product_name', 'category')
```
