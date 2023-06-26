from django.http import HttpResponse
from django.shortcuts import render


def index(request):
    return HttpResponse('<h1>Страница Чобанов<h1>')


def categories(request, catid):
    return HttpResponse(f'<h1>Виды Чобанов</h1><p>{catid}<p>')

