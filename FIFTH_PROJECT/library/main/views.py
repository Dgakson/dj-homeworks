from rest_framework import viewsets
from rest_framework.decorators import api_view
from rest_framework.generics import RetrieveAPIView, UpdateAPIView, DestroyAPIView, CreateAPIView, ListAPIView
from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework import status

from main.models import Book, Order
from main.serializers import BookSerializer, OrderSerializer


@api_view(['GET'])
def books_list(request):
    """получите список книг из БД
    отсериализуйте и верните ответ
    """
    books = Book.objects.all()
    ser = BookSerializer(books, many=True)
    return Response(ser.data)


# class CreateBookView(APIView):
#     def post(self, request):
#         # получите данные из запроса
#         serializer = BookSerializer(data=request.data) #передайте данные из запроса в сериализатор
#
#         if serializer.is_valid(raise_exception=True): #если данные валидны
#             serializer.save()
#             return Response('Книга успешно создана') # возвращаем ответ об этом
#
#         return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)  # Возвращаем ошибки валидации, если они есть
class BookListView(ListAPIView):
    queryset = Book.objects.all()
    serializer_class = BookSerializer


class CreateBookView(CreateAPIView):
    queryset = Book.objects.all()
    serializer_class = BookSerializer

class BookDetailsView(RetrieveAPIView):
    # реализуйте логику получения деталей одного объявления
    queryset = Book.objects.all()
    serializer_class = BookSerializer

class BookUpdateView(UpdateAPIView):
    # реализуйте логику обновления объявления
    queryset = Book.objects.all()
    serializer_class = BookSerializer


class BookDeleteView(DestroyAPIView):
    # реализуйте логику удаления объявления
    queryset = Book.objects.all()
    serializer_class = BookSerializer


class OrderViewSet(viewsets.ModelViewSet):
    # реализуйте CRUD для заказов
    queryset = Order.objects.all()
    serializer_class = OrderSerializer

