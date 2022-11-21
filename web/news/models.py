from django.db import models
from django.urls import reverse

# Create your models here.
class article(models.Model):
    title = models.CharField('Название', max_length=50)
    anons = models.CharField('Краткое описание', max_length=150)
    description = models.TextField('Полное описание')
    date = models.DateField('Дата публикации', auto_now_add=True)

    def __str__(self):
        return f'Статья: {self.title}'

    class Meta:
        verbose_name = 'Cтатья'
        verbose_name_plural = 'Cтатьи'

    def get_absolute_url(self):
        return f'{self.id}'
        #return reverse('news', kwargs={'news_id': self.pk})
