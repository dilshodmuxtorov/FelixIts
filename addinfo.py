import os
import json
import django

os.environ.setdefault("DJANGO_SETTINGS_MODULE", "config.settings")  
django.setup()

from warehouse.models import ProductMaterialModel, MaterialModel, WarehouseModel, ProductModel

def add_data_from_json_file(json_file_path):
    with open(json_file_path, 'r') as file:
        data = json.load(file)

    for product in data['productmodel']['product']:
        product_name = product['product_name']
        product_code = product['product_code']
        product_instance = ProductModel.objects.create(product_name=product_name, product_code=product_code)

    for material in data['materialmodel']['materials']:
        material_name = material['material_name']
        material_instance = MaterialModel.objects.create(material_name=material_name)

    for product_material in data['productmaterialmodel']['productmaterial']:
        product_id = product_material['product_id']
        material_id = product_material['material_id']
        quantity = product_material['quantity']
        product_instance = ProductModel.objects.get(id=product_id) 
        material_instance = MaterialModel.objects.get(id=material_id)
        ProductMaterialModel.objects.create(product_id=product_instance, material_id=material_instance, quantity=quantity)

    for warehouse in data['warehousemodel']['warehouse']:
        material_id = warehouse['material_id']
        remainder = warehouse['remainder']
        price = warehouse['price']
        material_instance = MaterialModel.objects.get(id=material_id)  
        WarehouseModel.objects.create(material_id=material_instance, remainder=remainder, price=price)

if __name__=="__main__":
    add_data_from_json_file('info.json')

