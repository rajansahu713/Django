from django.urls import path, include
from .views import ProductCreateView, ProductUpdateView, ProductDeleteView, ProductListView, ProductDetailView
urlpatterns = [
    path('',ProductListView.as_view(), name='list'),
    path('create/',ProductCreateView.as_view(), name='create'),
    path('<int:pk>/',ProductDetailView.as_view(), name='detail'),
    path('<int:pk>/update/',ProductUpdateView.as_view(), name='update'),
    path('<int:pk>/delete/',ProductDeleteView.as_view(), name='delete'),
    

]