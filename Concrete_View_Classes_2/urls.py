from django.urls import path, include
from .views import ProductList
urlpatterns = [
    path('<int:pk>', ProductList.as_view(), name='list'),

]