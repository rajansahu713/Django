from django.urls import path, include
from .views import ProductList, ProductDetail
urlpatterns = [
    path('', ProductList.as_view(), name='list'),
    path('<slug:pk>/', ProductDetail.as_view(), name='detail'),

]