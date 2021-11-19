"""app URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('admin/', admin.site.urls),
    path('api-auth/', include('rest_framework.urls')),
    path('fn_api/', include('fn_api.urls')),
    path('apiview/', include('apiview_api.urls')),
    path('viewset/', include('viewset_api.urls')),
    path("Generic/", include("generic_apiview_api.urls")),
    path("concrete/", include("Concrete_View_Classes.urls")),
    path("concrete_1/",include("Concrete_View_Classes_1.urls")),
    path("concrete_2/",include("Concrete_View_Classes_2.urls")),
    path("viewset_modelviewset/",include("viewset_modelviewset.urls")),
]
