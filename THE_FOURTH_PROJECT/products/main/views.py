from django.shortcuts import render
from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework.views import APIView

from django.http import Http404

from .models import Product, Review
from main.serializers import ReviewSerializer, ProductListSerializer, ProductDetailsSerializer




@api_view(['GET'])
def products_list_view(request):
    """реализуйте получение всех товаров из БД
    реализуйте сериализацию полученных данных
    отдайте отсериализованные данные в Response"""

    products = Product.objects.all()
    ser = ProductListSerializer(products, many=True)
    return Response(ser.data)


class ProductDetailsView(APIView):
    def get(self, request, product_id):
        """реализуйте получение товара по id, если его нет, то выдайте 404
        реализуйте сериализацию полученных данных
        отдайте отсериализованные данные в Response"""

        try:
            product = Product.objects.get(pk=product_id)

            ser = ProductDetailsSerializer(product, many=False)
            return Response(ser.data)
        except Product.DoesNotExist:
            raise Http404('Product not found')
        

# доп задание:
class ProductFilteredReviews(APIView):
    def get(self, request, product_id):
        """обработайте значение параметра mark и
        реализуйте получение отзывов по конкретному товару с определённой оценкой
        реализуйте сериализацию полученных данных
        отдайте отсериализованные данные в Response"""

        mark = request.GET.get('mark', None)
        # Получаем продукт по product_id
        try:
            product = Product.objects.get(pk=product_id)
        except Product.DoesNotExist:
            return Response({"error": "Product not found."})

        # Фильтруем отзывы по оценке, если mark указан
        if mark is not None:
            try:
                mark = int(mark)  # Преобразуем mark в целое число
                details = product.details.filter(mark=mark)  # Фильтруем отзывы по оценке
            except ValueError:
                return Response({"error": "Invalid mark value."})
        else:
            details = product.details.all()  # Если mark не указан, получаем все отзывы

        # Сериализуем данные
        serializer = ReviewSerializer(details, many=True)

        # Возвращаем сериализованные данные в ответе
        return Response(serializer.data)