from django.db import models
from django.core.validators import MaxValueValidator, MinValueValidator

class review(models.Model):
    firstName = models.CharField(max_length=40, verbose_name='Имя', help_text='Иван')
    lastName = models.CharField(max_length=100,verbose_name="Фамилия", help_text='Иванов')
    birth = models.DateField(blank=True, verbose_name="Дата рождения", help_text='DD-MM-YYYY')
    grade = models.PositiveSmallIntegerField(
        default=1,
        validators=[
            MaxValueValidator(10),
            MinValueValidator(1)
        ],
        help_text="Оценка от 1 до 10",
        verbose_name="Оценка"
    )
    text = models.TextField(verbose_name="Отзыв", help_text='Напишите свой отзыв...')
    createdAt = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"Отзыв №{self.pk}"

    class Meta:
        verbose_name="Отзыв"
        verbose_name_plural='Отзывы'
