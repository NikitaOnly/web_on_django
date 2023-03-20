from django.contrib.auth.models import User
from django.db import models


class Task(models.Model):
    title = models.CharField('the name', max_length=250)
    task = models.TextField('description')
    objects = None

    def __str__(self):
        return self.title

    class Meta:
        verbose_name = "Задача"
        verbose_name_plural = "Задачи"


class SalesOrder(models.Model):
    description = models.CharField(max_length=200)
    amount = models.IntegerField()
    user = models.ForeignKey(User, on_delete=models.CASCADE, null=True)
    objects = None

    def __str__(self):
        return self.description


class DateOrder(models.Model):
    date_of_order = models.DateField()
    time_order = models.DateTimeField()


class Payments(models.Model):
    sale_pay = models.FloatField()
