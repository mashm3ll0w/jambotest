from django.urls import path

from . import views

urlpatterns = [
    path("", views.index, name="index"),
    path("customers/", views.customers, name="customers"),
    path("customer/<int:pk>/", views.customers, name="customer"),
    path("businesses/", views.businesses, name="businesses"),
    path("business/<int:pk>/", views.business, name="business"),
]
