from django.urls import path
from . import views

urlpatterns = [
    path('', views.products, name="products"),
    path('<int:pk>/<slug:slug>/', views.productsdetail, name="productsdetail"),
    
]