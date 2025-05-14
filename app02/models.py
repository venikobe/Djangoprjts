from django.db import models

# Create your models here.
class TaskModel(models.Model):
    taskQuestion = models.CharField(default="Сколько записей о переработках в день Х?", verbose_name="Формулировка задачи")
    overworkInput = models.CharField(default="арьуз, вторник, 4| дыня, вторник, 2", verbose_name="Ввод записей")
    dayInput = models.CharField(default="вторник", verbose_name="Ввод дня")
    result = models.IntegerField(verbose_name="Результат", default=-1)
    currenttime = models.DateTimeField(verbose_name='Дата изменения', auto_now=True)
