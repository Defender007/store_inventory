"""
URL configuration for inventory_management project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.0/topics/http/urls/
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
from django.urls import path
from inventory import views
from drf_spectacular.views import SpectacularAPIView, SpectacularRedocView, SpectacularSwaggerView

urlpatterns = [
    path('admin/', admin.site.urls),
    path('api/contacts/', views.ContactListCreateAPIView.as_view(), name='contact-list-create'),
    path('api/contacts/<int:pk>/', views.ContactRetrieveUpdateDestroyAPIView.as_view(), name='contact-detail'),
    path('api/suppliers/', views.SupplierListCreateAPIView.as_view(), name='supplier-list-create'),
    path('api/suppliers/<int:pk>/', views.SupplierRetrieveUpdateDestroyAPIView.as_view(), name='supplier-detail'),
    path('api/items/', views.ItemListCreateAPIView.as_view(), name='item-list-create'),
    path('api/items/<int:pk>/', views.ItemRetrieveUpdateDestroyAPIView.as_view(), name='item-detail'),
    path('api/schema/', SpectacularAPIView.as_view(), name='schema'),
    path('api/docs/', SpectacularSwaggerView.as_view(url_name='schema'), name='swagger-ui'),
    path('api/redoc/', SpectacularRedocView.as_view(url_name='schema'), name='redoc'),
]
