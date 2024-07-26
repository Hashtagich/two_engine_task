from django.contrib import admin
from .models import Task


# Register your models here.


# MODELS


@admin.register(Task)
class TaskAdmin(admin.ModelAdmin):
    list_display = (
        'id',
        'name',
        'status',
        'description',
        'datetime_create'
    )
