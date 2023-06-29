from django.http import HttpResponse, HttpResponseNotFound
from django.shortcuts import render, redirect

from .models import *

menu = ['О сайте', 'Добавить чобана', 'Обратная связь', 'Войти']
def index(request):
    posts = Choban.objects.all()
    return render(request, 'Choban/index.html', {'posts':posts, 'menu': menu, 'title': 'Главная страница'})

def about(request):
    return render(request, 'Choban/about.html', {'menu': menu, 'title' : 'О сайте'})


def categories(request, catid):
    if request.POST:
        print(request.POST)
    return HttpResponse(f'<h1>Виды Чобанов</h1><p>{catid}<p>')


def archive(request, year):
    if int(year) > 2020:
        return redirect('/', permanent=False)
    return HttpResponse(f'<h1>Архив по годам</h1><p>{year}<p>')


def pageNotFound(request, exception):
    return HttpResponseNotFound('<h1>Страница не найдена<h1>')
