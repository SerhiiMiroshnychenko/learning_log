"""Defines URL patterns for learning_logs --- Визначає шаблони URL для learning_logs"""

from django.urls import path  # Імпорт path - потрібна, щоб пов'язати URL з видами

from . import views  # Імпорт модуля views. Крапка каже python шукати його в тій же самій теці

app_name = 'learning_logs'  # Змінна app_name допомогає django відрізнити цей urls.py
# від файлів з такою ж назвою в цьому проєкті
urlpatterns = [  # Змінна urlpatterns - список індивідуальних сторінок,
    # до яких можна звернутися із застосунку learning_logs:
    # Головна сторінка:
    path('', views.index, name='index'),  # Функція path() повертає регулярний вираз URL і приймає
    # три аргументи:
    # перший(пустий string) - допомагає django правильно маршрутизувати поточний запит
    # другий(views.index) - описує, яку функцію з views.py треба викликати.
    # третій(name='index') - дає ім'я "index" цьому регулярному виразу URL
    # Сторінка, що показує всі теми:
    path('topics/', views.topics, name='topics'),
]

