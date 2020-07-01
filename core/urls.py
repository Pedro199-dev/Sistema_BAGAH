from django.urls import path
from . import views

urlpatterns = [
    path("", views.index, name="index"),
    path("about", views.about, name="about"),
    path("services", views.services, name="services"),
    path("events", views.events, name="events"),
    path("products", views.products, name="products"),
    
]