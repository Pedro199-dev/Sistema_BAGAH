from django.contrib import admin
from .models import ProductCart
# Register your models here.
class CartAdmin(admin.ModelAdmin):
    readonly_fields = ('created', 'updated')

admin.site.register(ProductCart, CartAdmin)
