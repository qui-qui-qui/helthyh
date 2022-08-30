from turtle import position, width
from django.db import models

class BaseWidget(models.Model):
    position = models.IntegerField(verbose_name='Положение', unique=True, blank=False, null=False)
    heigth = models.FloatField(verbose_name='Высота', blank=False)
    width = models.FloatField(verbose_name='Ширина', blank=False)
    mode = models.BooleanField(verbose_name='Присутствие', blank=False)

    class Meta:
        db_table = 'base_widget'