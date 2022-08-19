from django.db import models

class Weight(models.Model):
    """Модель веса пользователя"""
    id = models.ForeignKey(to=..., primary_key=True)
    weight = models.FloatField(verbose_name='Вес', blank=True)

    class Meta:
        db_table = 'weight'

class Anthropometry(models.Model):
    """"Модель антропометрических данных пользователя"""
    id = models.ForeignKey(to=..., primary_key=True)
    forearm = models.FloatField(verbose_name='Предплечье', blank=True) 
    neck = models.FloatField(verbose_name='Шея', blank=True)
    shoulder_belt = models.FloatField(verbose_name='Плечевой пояс', blank=True)
    breast = models.FloatField(verbose_name='Грудь', blank=True)
    belly = models.FloatField(verbose_name='Живот', blank=True)
    pelvis = models.FloatField(verbose_name='Таз', blank=True)
    hip = models.FloatField(verbose_name='Бедро', blank=True)
    height = models.FloatField(verbose_name='Рост', blank=True)

    class Meta:
        db_table = 'anthropometry'

class Nutritional_energy_value(models.Model):
    """"Модель антропометрических данных пользователя"""
    id = models.ForeignKey(to=..., primary_key=True)
    proteins = models.PositiveIntegerField(verbose_name='Белки', blank=True)
    fats = models.PositiveIntegerField(verbose_name='Жиры', blank=True)
    carbohydrates = models.PositiveIntegerField(verbose_name='Углеводы', blank=True)
    calories = models.PositiveIntegerField(verbose_name='Калории', blank=True)

    class Meta:
        db_table = 'nutritional_energy_value'
    