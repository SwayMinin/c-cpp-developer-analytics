from django.shortcuts import render
from .models import *


def __transpose(list_of_lists):
    transposed_tuples = list(zip(*list_of_lists))
    return [list(sublist) for sublist in transposed_tuples]


def __dict_from_table(table, name):
    return {'name': name,
            'headers': [row.name for row in table.rows.all()],
            'rows': __transpose([row.text.split() for row in table.rows.all()]),
            'images': table.images}


def __get_active_tabs(active_index):
    tabs = [False for _ in range(5)]
    tabs[active_index] = True
    return tabs


def index(request):
    data = {
        'title': 'Главная',
        'blocks': TextBlock.objects.order_by('order'),
        'active_tabs': __get_active_tabs(0),
    }
    return render(request, 'main/index.html', data)


def demand(request):
    mean_median_dict = __dict_from_table(Table.objects.all()[0], 'Уровень зарплат по годам')
    vacancies_count_dict = __dict_from_table(Table.objects.all()[1], 'Количество вакансий по годам')
    data = {
        'title': 'Востребованность',
        'page_theme': 'Динамика уровня зарплат по годам',
        'tables': [mean_median_dict, vacancies_count_dict],
        'images': Image.objects.all(),
        'active_tabs': __get_active_tabs(1),
    }
    return render(request, 'main/demand.html', data)


def geography(request):
    data = {
        'title': 'География',
        'active_tabs': __get_active_tabs(2),
    }
    return render(request, 'main/geography.html', data)


def skills(request):
    data = {
        'title': 'Навыки',
        'active_tabs': __get_active_tabs(3),
    }
    return render(request, 'main/skills.html', data)


def latest(request):
    data = {
        'title': 'Последние вакансии',
        'active_tabs': __get_active_tabs(4),
    }
    return render(request, 'main/latest.html', data)
