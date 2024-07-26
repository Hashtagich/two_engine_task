from rest_framework import serializers
from .models import Task


class TaskSerializer(serializers.ModelSerializer):
    datetime_create = serializers.DateTimeField(format='%d.%m.%Y %H:%M:%S')

    class Meta:
        model = Task
        fields = (
            'id',
            'name',
            'status',
            'description',
            'datetime_create',
        )

    read_only_fields = ('id', 'datetime_create',)
