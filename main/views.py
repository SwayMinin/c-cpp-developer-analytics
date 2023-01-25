from django.shortcuts import render
from .models import *


def __transpose(list_of_lists):
    transposed_tuples = list(zip(*list_of_lists))
    return [list(sublist) for sublist in transposed_tuples]


def __dict_from_table(table):
    return {'name': table.name,
            'headers': [row.name for row in table.rows.all()],
            'rows': __transpose([[cell.replace('_', ' ') for cell in row.text.split()] for row in table.rows.all()]),
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
    mean_median_dict = __dict_from_table(Table.objects.all()[0])
    vacancies_count_dict = __dict_from_table(Table.objects.all()[1])
    data = {
        'title': 'Востребованность',
        'page_theme': 'Динамика уровня зарплат по годам',
        'tables': [mean_median_dict, vacancies_count_dict],
        'images': Image.objects.all(),
        'active_tabs': __get_active_tabs(1),
    }
    return render(request, 'main/demand.html', data)


def geography(request):
    top_salary_cities = __dict_from_table(Table.objects.all()[2])
    cities_share = __dict_from_table(Table.objects.all()[3])
    data = {
        'title': 'География',
        'tables': [top_salary_cities, cities_share],
        'active_tabs': __get_active_tabs(2),
    }
    return render(request, 'main/geography.html', data)


def skills(request):
    top_skills = __dict_from_table(Table.objects.all()[4])
    top_with_place = __dict_from_table(Table.objects.all()[5])
    data = {
        'title': 'Навыки',
        'tables': [top_skills, top_with_place],
        'active_tabs': __get_active_tabs(3),
    }
    return render(request, 'main/skills.html', data)


def latest(request):
    data = {
        'title': 'Последние вакансии',
        'active_tabs': __get_active_tabs(4),
    }
    return render(request, 'main/latest.html', data)
