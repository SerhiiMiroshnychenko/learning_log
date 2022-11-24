from django.shortcuts import render

from .models import Topic


# Create your views here:
def index(request):
    """Головна сторінка "Журналу спостережень"."""
    return render(request, 'learning_logs/index.html')


def topics(request):  # Функція topics() приймає один параметр: об'єкт запиту отриманий від сервера
    """Показує всі теми"""
    topics = Topic.objects.order_by('date_added')  # робимо запит до бази даних: просимо всі об'єкти
    # Topic, впорядковані за атрибутом date_added.
    context = {'topics': topics}  # Визначаємо контекст, який відправимо до шаблону
    return render(request, 'learning_logs/topics.html', context)  # будуємо сторінку



