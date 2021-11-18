from django.urls import path, include
from . import views
urlpatterns = [
    path('', views.ProductGenericview.as_view(), name='product_list'),
    path('<int:pk>/', views.ProductGenericview_1.as_view(), name='product_detail'),
]