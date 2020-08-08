from django.urls import path
from . import views

urlpatterns = [
    path('', views.products, name="products"),
    path('single/<int:product_id>', views.productsdetail, name="productsdetail"),
    path('checkout/', views.checkout, name="checkout"),
    path('payment/', views.payment, name="payment"),
    path('category/<int:category_id>', views.category, name="category"),
    
]