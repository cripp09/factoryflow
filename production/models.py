from django.db import models
from django.urls import reverse


class Category(models.Model):
    name = models.CharField(max_length=200,
                            verbose_name='Категория')
    slug = models.SlugField(max_length=200)

    class Meta:
        ordering = ['name']
        indexes = [
            models.Index(fields=['name']),
        ]
        verbose_name = 'Категория'
        verbose_name_plural = 'Категории'

    def __str__(self):
        return self.name
    
    def get_absolute_url(self):
        pass

class Product(models.Model):
    category = models.ForeignKey(Category,
                                 related_name='products',
                                 on_delete=models.CASCADE,
                                 verbose_name='Категория')
    article = models.CharField(max_length=10,
                               verbose_name='Артикул')
    name = models.CharField(max_length=200,
                                verbose_name='Название')
    slug = models.SlugField(max_length=200,
                                verbose_name='Транслит')
    proteins = models.DecimalField(max_digits=10,
                                decimal_places=1,
                                verbose_name='Белки')
    fats = models.DecimalField(max_digits=10,
                                decimal_places=1,
                                verbose_name='Жиры')
    shelf_life = models.IntegerField(max_length=2,
                                     verbose_name='Срок годности в мес.')
    gost = models.CharField(max_length=100,
                            verbose_name='ГОСТ/ТУ')
    halal = models.BooleanField(default=True,
                                verbose_name='Халяль')
    ean_13 = models.BooleanField(default=False)
    barcode_e13 = models.CharField(max_length=13,
                                   verbose_name='ШК от заказчика')
    
    image = models.ImageField(upload_to='products/%Y/%m/%d',
                                blank=True,
                                verbose_name='Изображение')
    description = models.TextField(blank=True,
                                   verbose_name='Описание')
    price = models.DecimalField(max_digits=10,
                                decimal_places=2,
                                verbose_name='Стоимость')
    available = models.BooleanField(default=True,
                                    verbose_name='Наличие')
    created = models.DateTimeField(auto_now_add=True,
                                   verbose_name='Дата и время создания')
    updated = models.DateTimeField(auto_now=True,
                                   verbose_name='Обновлено')

    class Meta:

        ordering = ['name']
        indexes = [
            models.Index(fields=['id', 'slug']),
            models.Index(fields=['article']),
            models.Index(fields=['name']),
            models.Index(fields=['-created']),
        ]
        verbose_name = 'Продукт'
        verbose_name_plural = 'Продукты'
    
    def __str__(self):
        return self.name
    
    def get_absolute_url(self):
        pass