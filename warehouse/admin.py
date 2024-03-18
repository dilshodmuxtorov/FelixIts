from django.contrib import admin
from .models import (
    ProductModel,
    MaterialModel,
    ProductMaterialModel,
    WarehouseModel
)

class ProductModelAdmin(admin.ModelAdmin):
    list_display = ['product_name','product_code','id']

class MaterialModelAdmin(admin.ModelAdmin):
    list_display = ['material_name','id']

class ProductMaterialModelAdmin(admin.ModelAdmin):
    list_display = ['product_id','material_id','quantity','id']

class WarehouseModelAdmin(admin.ModelAdmin):
    list_display = ['material_id','remainder','price','id']

admin.site.register(ProductModel,ProductModelAdmin)
admin.site.register(MaterialModel,MaterialModelAdmin)
admin.site.register(ProductMaterialModel,ProductMaterialModelAdmin)
admin.site.register(WarehouseModel,WarehouseModelAdmin)
