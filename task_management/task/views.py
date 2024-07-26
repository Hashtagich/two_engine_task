from drf_spectacular.utils import extend_schema
from rest_framework import viewsets
from rest_framework.response import Response

from .models import Task
from .serializers import TaskSerializer


@extend_schema(tags=['Задачи'])
class TaskViewSet(viewsets.ModelViewSet):
    serializer_class = TaskSerializer
    queryset = Task.objects.all()

    @extend_schema(summary="API для получения всех задач")
    def list(self, request, *args, **kwargs):
        queryset = self.queryset  # на случай расширения функционала
        serializer = TaskSerializer(queryset, many=True)
        return Response(serializer.data)

    @extend_schema(summary="API для получения информации о задаче по её ID")
    def retrieve(self, request, pk=None, *args, **kwargs):
        return super().retrieve(request, *args, **kwargs)

    @extend_schema(summary="API для создания задачи")
    def create(self, request, *args, **kwargs):
        return super().create(request, *args, **kwargs)

    @extend_schema(summary="API для обновления задачи")
    def update(self, request, *args, **kwargs):
        return super().update(request, *args, **kwargs)

    @extend_schema(summary="API для частичного обновления задачи")
    def partial_update(self, request, *args, **kwargs):
        return super().partial_update(request, *args, **kwargs)

    @extend_schema(summary="API для удаления задачи")
    def destroy(self, request, *args, **kwargs):
        return super().destroy(request, *args, **kwargs)
