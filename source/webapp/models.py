from django.db import models

STATUS_CHOICES = [('new', 'Новая'), ('in_progress', 'В процессе'),  ('done', 'Сделано')]


class Task(models.Model):
    description = models.TextField(max_length=100, null=False, blank=False, verbose_name="Описание")
    status = models.CharField(max_length=25, choices=STATUS_CHOICES, default='new', verbose_name='Статус')
    due_date = models.DateField(blank=True, null=True, verbose_name='Дата выполнения')

    def __str__(self):
        return f"{self.pk}. {self.description}: {self.status}"

    class Meta:
        db_table = "todolist"
        verbose_name = "Список"
        verbose_name_plural = "Список"

    def is_valid(self):
        pass
