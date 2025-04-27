"""
URL configuration for myshop project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.2/topics/http/urls/
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
from django.urls import path
from . import views

urlpatterns = [
    path('phones/', views.PhoneListView.as_view(), name='phone-list'),
    path('phones/<int:id>', views.PhoneDetailView.as_view(), name='phone-detail'),
    path('delete/<int:id>', views.PhoneDeleteView.as_view(), name='phone-delete'),
    path('newPhone/', views.PhoneNewView.as_view(), name='phone-new'),
    path('colors/', views.ColorListView.as_view(), name='colors-list'),
    path('brands/', views.BrandListView.as_view(), name='brands-list'),
    path('so/', views.SoListView.as_view(), name='so-list'),
    path('cameras/', views.CameraListView.as_view(), name='camera-list'),
]

