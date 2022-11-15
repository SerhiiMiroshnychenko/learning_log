from django.db import models


# Create your models here.
class Topic(models.Model):  # створюємо клас Topic, що наслідує Model - батьківський клас django
    """Тема яку вивчає користувач"""
    text = models.CharField(max_length=200)  # елемент даних, що складається з символів або тексту
    # max_length=200 --> максимальна довжина
    data_added = models.DateTimeField(auto_now_add=True)  # елемент даних де записано дату та час
    # auto_now_add=True --> автоматично встановлює значення цього атрибуту в поточну дату та час

    def __str__(self):
        """Повернути рядкове представлення моделі"""
        return self.text
