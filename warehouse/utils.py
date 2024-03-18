import json
from .models import ProductMaterialModel,MaterialModel, WarehouseModel, ProductModel

lastresult ={}
allmaterials = []
def calculate_materials(product_name, quantity):
    result = {"product_name": product_name, "product_qty": quantity, "product_materials": []}
    materials = ProductMaterialModel.objects.filter(product_id__product_name=product_name)
    for material in materials:
        warehouses = WarehouseModel.objects.filter(material_id__material_name=material.material_id.material_name).order_by('id')
        need = quantity * material.quantity

        for warehouse in warehouses:
            if lastresult == {}:
                if warehouse.remainder >= need:
                    result['product_materials'].append({
                        "warehouse_id": warehouse.id,
                        "material_name": material.material_id.material_name,
                        "qty": need,
                        "price": warehouse.price
                    })      
                    need = 0            
                    break
                else:
                    result['product_materials'].append({
                        "warehouse_id": warehouse.id,
                        "material_name": material.material_id.material_name,
                        "qty": warehouse.remainder,
                        "price": warehouse.price
                    })
                    need = need-warehouse.remainder
            else:
                if material.material_id.material_name  in allmaterials:
                    for i in lastresult["product_materials"]:
                        if i["warehouse_id"]==warehouse.id and i['qty']==warehouse.remainder:
                            break
                        elif i['qty']<warehouse.remainder and i["material_name"] == warehouse.material_id.material_name and i["warehouse_id"]==warehouse.id:
                            if warehouse.remainder-i['qty'] >= need:
                                result['product_materials'].append({
                                    "warehouse_id": warehouse.id,
                                    "material_name": material.material_id.material_name,
                                    "qty": need,
                                    "price": warehouse.price
                                })  
                                need = 0            
                                break
                            else:
                                result['product_materials'].append({
                                    "warehouse_id": warehouse.id,
                                    "material_name": material.material_id.material_name,
                                    "qty": warehouse.remainder- i['qty'],
                                    "price": warehouse.price
                                })
                                need = need-warehouse.remainder+i["qty"]
                else:
                    if warehouse.remainder >= need:
                        result['product_materials'].append({
                            "warehouse_id": warehouse.id,
                            "material_name": material.material_id.material_name,
                            "qty": need,
                            "price": warehouse.price
                        })      
                        need = 0            
                        break
                    else:
                        result['product_materials'].append({
                            "warehouse_id": warehouse.id,
                            "material_name": material.material_id.material_name,
                            "qty": warehouse.remainder,
                            "price": warehouse.price
                        })
                        need = need-warehouse.remainder


        if need!=0 and need!=quantity * material.quantity:
            result['product_materials'].append({
                        "warehouse_id": None,
                        "material_name": material.material_id.material_name,
                        "qty": need,
                        "price": None
                    })  
        if  material.material_id.material_name not in allmaterials:
            allmaterials.append(material.material_id.material_name)  
    print(allmaterials)
      
    lastresult.update(result)
    return result



