from django.urls import path
from . import views

urlpatterns = [
    path('carslist/<int:car_id>', views.car_item, name='caritem'),
    path('carslist', views.cars_list, name='carslist'),
    path('', views.mainpage, name='rental')
]