from rest_framework.permissions import IsAuthenticated
from rest_framework.viewsets import ModelViewSet
from rest_framework.throttling import AnonRateThrottle
from rest_framework.response import Response
from rest_framework import status

from advertisements.models import Advertisement
from advertisements.serializers import AdvertisementSerializer
from advertisements.permissions import IsOwnerOrReadOnly

from advertisements.filters import AdvertisementFilter
from django_filters import rest_framework as filters




class AdvertisementViewSet(ModelViewSet):
    """ViewSet для объявлений."""
    queryset = Advertisement.objects.all()
    serializer_class = AdvertisementSerializer
    permission_classes = [IsOwnerOrReadOnly]
    throttle_classes = [AnonRateThrottle]

    filter_backends = [filters.DjangoFilterBackend]
    filterset_fields = ['creator', 'status']
    filterset_class = AdvertisementFilter

    def get_permissions(self):

        """Получение прав для действий."""
        if self.action == 'create':
            return [IsAuthenticated()]
        elif self.action in ['update', 'partial_update', 'destroy']:
            return [IsOwnerOrReadOnly()]
        return []

    # def perform_create(self, serializer):
    #     serializer.save(creator=self.request.user)
    #
    # def perform_update(self, serializer):
    #     """Сохранение обновленного объявления."""
    #     serializer.save(creator=self.request.user)
    #
    # def destroy(self, request, *args, **kwargs):
    #     """Удаление объявления, доступно только владельцу."""
    #     instance = self.get_object()  # Получаем объект для удаления
    #
    #     # Проверяем, является ли текущий пользователь владельцем
    #     if instance.creator != request.user:
    #         return Response(
    #             {"detail": "У вас нет прав на удаление этого объявления."}
    #         )
    #
    #     self.perform_destroy(instance)  # Удаляем объект
    #     return Response({"detail": "Объявление удалено."})
