from django.shortcuts import render
from .models import *


def __transpose(list_of_lists):
    transposed_tuples = list(zip(*list_of_lists))
    return [list(sublist) for sublist in transposed_tuples]


def __dict_from_table(table):
    table_dict = {'headers': [row.name for row in table.rows.all()],
                  'rows': [row.text.split() for row in table.rows.all()]}
    table_dict['rows'] = __transpose(table_dict['rows'])
    return table_dict


def index(request):
    description = TextBlock.objects.order_by('order')
    for block in description:
        block.text = block.text.split(';')
    data = {
        'title': 'C/C++ Разработчик',
        'description': description,
    }
    return render(request, 'main/index.html', data)


def demand(request):
    mean_median_table = Table.objects.get(name='Средняя и медианная зарплата по годам')
    data = {
        'title': 'Востребованность',
        'page_theme': 'Динамика уровня зарплат по годам',
        'mean_table': __dict_from_table(mean_median_table),
    }
    return render(request, 'main/demand.html', data)


def geography(request):
    return render(request, 'main/geography.html', {'title': 'География'})


def skills(request):
    return render(request, 'main/skills.html', {'title': 'Навыки'})


def latest(request):
    return render(request, 'main/latest.html', {'title': 'Последние вакансии'})
