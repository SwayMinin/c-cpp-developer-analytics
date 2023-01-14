from django.shortcuts import render


def index(request):
    return render(request, 'main/index.html', {'title': 'C/C++ Разработчик'})


def demand(request):
    return render(request, 'main/demand.html', {'title': 'Востребованность'})


def geography(request):
    return render(request, 'main/geography.html', {'title': 'География'})


def skills(request):
    return render(request, 'main/skills.html', {'title': 'Навыки'})


def latest(request):
    return render(request, 'main/latest.html', {'title': 'Последние вакансии'})


