from django.contrib.auth.models import User
from django.db import models


class Todo(models.Model):
    title = models.CharField(max_length=100, verbose_name = 'Дело')
    description = models.TextField(blank=True, verbose_name= 'Описание дела')
    published = models.DateTimeField(auto_now_add=True, verbose_name= "Дата создания")
    date_completed = models.DateTimeField(null=True, verbose_name= "Дата выполнения", blank = True)
    important = models.BooleanField(default=False, verbose_name= "Важность")
    user = models.ForeignKey(User, on_delete=models.CASCADE, db_index=True, verbose_name= 'Кто оставил')
    class Meta:
        verbose_name = 'Задача'
        verbose_name_plural = "Задачи"
    def __str__(self):
        return self.title
