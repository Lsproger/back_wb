from django.contrib import admin
from back_wb.wb_api.models import Product

@admin.register(Product)
class ProductAdmin(admin.ModelAdmin):
    pass