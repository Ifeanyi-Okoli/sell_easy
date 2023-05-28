from django.contrib import admin
from .models import Store, Product, Category, Rating

class StoreAdmin(admin.ModelAdmin):
    list_display = ('name', 'tagline', 'total_products')
    list_filter = ('name',)

class ProductAdmin(admin.ModelAdmin):
    list_display = ('name', 'price', 'store', 'category')
    list_filter = ('category', 'store')
    list_per_page = 10

admin.site.register(Store, StoreAdmin)
admin.site.register(Product, ProductAdmin)
admin.site.register(Category)
admin.site.register(Rating)
