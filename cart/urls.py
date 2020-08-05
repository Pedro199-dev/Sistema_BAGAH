from django.urls import path
from . import views 


urlpatterns = [
    path('', views.show, name="cart"),
    path('^add/$', views.add, name="shopping-cart-add"),
    path('^remove/$', views.remove, name="shopping-cart-remove"),
    path('^show/$', views.show, name="shopping-cart-show"),
]

