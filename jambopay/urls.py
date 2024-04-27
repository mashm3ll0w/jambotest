from django.urls import path

from . import views

urlpatterns = [
    path("", views.index, name="index"),
    path("customers/", views.customers, name="customers"),
    path("customers/<int:pk>/", views.customer, name="customer"),
    path("businesses/", views.businesses, name="businesses"),
    path("businesses/<int:pk>/", views.business, name="business"),
]
