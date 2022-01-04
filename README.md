# Django

In this repo i have perform CRUD operation in multiple ways
1. Funtion base view
2. Apiview
3. Generic Apiview
4. Viewset
5. ModelViewset
6. Concrete Apiview

### Function Base View
> Function based views are usually chosen when we want to highly customize the typical view logic since it is easier to follow the sequence of actions they describe.

### Apiview
> With APIview you code methods etc for the different HTTP call methods such as post, get, put etc. These come with no standard configuration, so you can customise to your needs.

### Generic Apiview
> Django’s generic views… were developed as a shortcut for common usage patterns… They take certain common idioms and patterns found in view development and abstract them so that you can quickly write common views of data without having to repeat yourself.

### Viewset
    Method Names reflect Database Model class actions/operations like list(),retrieve(),create(),update(),partial_update() and destroy()
    not required to map views to URLs explicitly. DefaultRouter will takes care URL mapping automatically
    Best suitable for developing simple APIs like developing CRUD interface for database models

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
