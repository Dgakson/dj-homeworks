from rest_framework import serializers
from .models import Book, Order


class BookSerializerTest(serializers.ModelSerializer):
    class Meta:
        model = Book
        fields = ['author', 'title', 'year']


class BookSerializer(serializers.ModelSerializer):
    class Meta:
        model = Book
        fields = '__all__'

    #доп задание
    def to_representation(self, instance):
        representation = super().to_representation(instance)
        representation['orders_count'] = instance.orders.count()
        return representation


class OrderSerializer(serializers.ModelSerializer):
    books = BookSerializerTest(many=True, read_only=True)

    class Meta:
        model = Order
        fields = ['id', 'user_name', 'days_count', 'date', 'books']

    # #доп задание
    def to_representation(self, instance):
        representation = super().to_representation(instance)

        return representation

