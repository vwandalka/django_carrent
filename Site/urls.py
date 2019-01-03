from django.urls import path
from . import views

urlpatterns = [
    path('', views.homepage, name='index'),
    path('about', views.about, name='about'),
    path('contact', views.contact, name='contact'),
    path('header', views.contact, name='header'),
    path('footer', views.contact, name='footer')
]