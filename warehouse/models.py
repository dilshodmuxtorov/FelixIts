from django.db import models


class ProductModel(models.Model):
    product_name = models.CharField(max_length = 255, default = "")
    product_code = models.CharField(max_length = 255, default = "")

    class Meta:
        db_table = 'products'
        verbose_name = 'Mahsulot'
        verbose_name_plural = 'Mahsulotlar'

    def __str__(self) -> str:
        return self.product_name


class MaterialModel(models.Model):
    material_name = models.CharField(max_length = 255, default = "")

    class Meta:
        db_table = 'materials'
        verbose_name = 'Xomashyo'
        verbose_name_plural = 'Xomashyolar'

    def __str__(self) -> str:
        return self.material_name
    
class ProductMaterialModel(models.Model):
    product_id = models.ForeignKey(ProductModel, on_delete = models.CASCADE)
    material_id = models.ForeignKey(MaterialModel, on_delete = models.CASCADE)
    quantity = models.FloatField(default = 0)
    
    
class WarehouseModel(models.Model):
    material_id = models.ForeignKey(MaterialModel, on_delete = models.CASCADE)
    remainder = models.IntegerField(default = 0 )
    price = models.IntegerField(default = 0)

    class Meta:
        db_table = 'warehouse'
        verbose_name = 'Partiya'
        verbose_name_plural = 'Partiyalar'
    

