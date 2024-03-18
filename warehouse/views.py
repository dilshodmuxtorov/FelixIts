from rest_framework.views import APIView
from rest_framework.response import Response
from .utils import calculate_materials
from .models import ProductModel
import json



class CalculateMaterialsView(APIView):
    def post(self, request):
        products_data = request.data.get('products')
        response_data = {"result": []}

        for product_data in products_data:
            product_name = product_data.get('name')
            product_qty = product_data.get('quantity')

            if ProductModel.objects.filter(product_name=product_name).exists():
                result = calculate_materials(product_name, product_qty)
                response_data['result'].append(result)

        return Response(response_data)
