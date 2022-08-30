from django.db import models
from django.conf import settings

class Account(models.Model):
    user = models.OneToOneField(settings.AUTH_USER_MODEL,on_delete=models.CASCADE)
    date_of_birth = models.DateField(blank=True, null=True)
    photo = models.ImageField(upload_to='users/%Y/%m/%d', blank=True)
    time_add = models.DateField(verbose_name='Время добавления',auto_now_add=True)

    def __str__(self):
        return 'Profile for user {}'.format(self.user.username)
    
    class Meta:
        db_table='helthyh_account'


class Weight(models.Model):
    """Модель веса пользователя"""
    user_id = models.ForeignKey(to='account.Account', on_delete=models.CASCADE)
    weight = models.FloatField(verbose_name='Вес', blank=True)
    time_add = models.DateField(verbose_name='Время добавления',auto_now_add=True)


    class Meta:
        db_table = 'weight'

class Anthropometry(models.Model):
    """"Модель антропометрических данных пользователя"""
    user_id = models.ForeignKey(to='account.Account', on_delete=models.CASCADE)
    forearm = models.FloatField(verbose_name='Предплечье', blank=True) 
    neck = models.FloatField(verbose_name='Шея', blank=True)
    shoulder_belt = models.FloatField(verbose_name='Плечевой пояс', blank=True)
    breast = models.FloatField(verbose_name='Грудь', blank=True)
    belly = models.FloatField(verbose_name='Живот', blank=True)
    pelvis = models.FloatField(verbose_name='Таз', blank=True)
    hip = models.FloatField(verbose_name='Бедро', blank=True)
    height = models.FloatField(verbose_name='Рост', blank=True)
    time_add = models.DateField(verbose_name='Время добавления',auto_now_add=True)


    class Meta:
        db_table = 'anthropometry'

class Nutritional_energy_value(models.Model):
    """"Модель антропометрических данных пользователя"""
    user_id = models.ForeignKey(to='account.Account', on_delete=models.CASCADE)
    proteins = models.PositiveIntegerField(verbose_name='Белки', blank=True)
    fats = models.PositiveIntegerField(verbose_name='Жиры', blank=True)
    carbohydrates = models.PositiveIntegerField(verbose_name='Углеводы', blank=True)
    calories = models.PositiveIntegerField(verbose_name='Калории', blank=True)
    time_add = models.DateField(verbose_name='Время добавления',auto_now_add=True)

    class Meta:
        db_table = 'nutritional_energy_value'
    