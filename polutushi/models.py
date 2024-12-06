from django.db import models
from django.urls import reverse

class Polutushi(models.Model):
    ear_number = models.CharField(max_length=15,
                                  blank=True, verbose_name='Ушной Номер')
    weight = models.DecimalField(max_digits=10, decimal_places=2)
    weighing_datetime = models.DateTimeField(auto_now_add=True)
    image = models.ImageField(upload_to='polutushi/%Y/%m/%d',
                              blank=True, verbose_name='Изображение')
    comment = models.TextField(blank=True,
                               verbose_name='Комментарии')
    class Meta:

        ordering = ['weighing_datetime']
        indexes = [
            models.Index(fields=['weighing_datetime']),
            models.Index(fields=['ear_number']),
        ]
        verbose_name = 'Полутуша'
        verbose_name_plural = 'Полутуши'
    
    def get_absolute_url(self):
            return reverse('polutushi_detail', kwargs={'id': self.id})
