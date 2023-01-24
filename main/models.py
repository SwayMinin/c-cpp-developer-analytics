from django.db import models


class TextBlock(models.Model):
    order = models.IntegerField('Порядковый номер', default=0)
    header = models.CharField('Заголовок блока', max_length=50)
    text = models.TextField('Текст блока')

    def __str__(self):
        return self.header

    class Meta:
        verbose_name = 'Блок'
        verbose_name_plural = 'Блоки'


class Row(models.Model):
    name = models.CharField('Название строки', max_length=250, default='')
    text = models.TextField('Текст строки')

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = 'Строка'
        verbose_name_plural = 'Строки'


class Table(models.Model):
    name = models.CharField('Название таблицы', max_length=250, default='')
    rows = models.ManyToManyField(Row)

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = 'Таблица'
        verbose_name_plural = 'Таблицы'
