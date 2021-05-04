from django.db import models


# Create your models here.
class Product(models.Model):
    name = models.TextField(verbose_name='Название')
    min_price = models.FloatField(verbose_name='Минимальная цена')
    max_price = models.FloatField(verbose_name='Максимальная цена')
    url = models.URLField(verbose_name='Ссылка', unique=True)
    type = models.URLField(verbose_name='Тип')

    class Meta:
        verbose_name = 'Продукт'
        verbose_name_plural = 'Продукты'
