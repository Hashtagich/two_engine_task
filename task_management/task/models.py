from django.db import models


# Create your models here.
class Task(models.Model):
    """Модель задачи."""
    CHOICE_STATUS = (
        ("new", 'В очереди'),
        ("in_progress", "В процессе"),
        ("done", "Завершена"),
    )
    name = models.CharField("Название задачи", max_length=60, null=True, default="Этап/задача №1")
    status = models.CharField("Статус", max_length=50, choices=CHOICE_STATUS, default="new")
    description = models.TextField("Описание задачи", null=True, blank=True)
    datetime_create = models.DateTimeField("Дата создания задачи", auto_now_add=True)

    def __str__(self):
        return f'{self.name} - {self.description[:20]} - {self.status}'

    class Meta:
        verbose_name = "Задача"
        verbose_name_plural = "Задачи"
        ordering = ('status', 'name')
