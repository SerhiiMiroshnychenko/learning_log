from django.shortcuts import render


# Create your views here:
def index(request):
    """Головна сторінка "Журналу спостережень"."""
    return render(request, 'learning_logs/index.html')
