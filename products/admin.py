from django.contrib import admin

from .models import Product, Category
# Register your models here.
class ProductAdmin(admin.ModelAdmin):
    readonly_fields = ('created', 'updated')

class CategoryProduct(admin.ModelAdmin):
    readonly_fields = ('created', 'updated')

    def post_categories(self, obj):
        return ", ".join([c.name for c in obj.categories.all().order_by("name")])
    post_categories.short_description = "Categorias"

admin.site.register(Category, CategoryProduct)
admin.site.register(Product)
