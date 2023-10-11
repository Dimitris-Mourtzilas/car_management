"""
URL configuration for djangoProject1 project.

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
from django.contrib import admin
from django.urls import path, include

from car.api import views
from car.api.views import CarRetrieveUpdateView
from car.views import index, list_cars, create_car, update_car, car_detail, delete_car

urlpatterns = [
    path('admin/', admin.site.urls),
    path('',index,name="home"),
    path('list-cars',list_cars,name="list_cars"),
    path('create-car',create_car,name='create_car'),
    path('update-car/<int:id>',update_car,name='update_car'),
    path('car/details/<int:pk>',car_detail,name="car_detail"),
    path('car/delete/<int:pk>',delete_car,name="delete_car"),
    path('api',views.CarViewSet.as_view(),name='cars'),
    path('api/<int:pk>',CarRetrieveUpdateView.as_view(),name="crud_car"),
]
