from django.contrib import admin
from .import models

# Register your models here.


@admin.register(models.Product)
class ProductAdmin(admin.ModelAdmin):
    list_display = ['product_name']
    search_fields = ['name']
