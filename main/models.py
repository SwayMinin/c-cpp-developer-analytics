from django.db import models


class TextBlock(models.Model):
    order = models.IntegerField('Порядковый номер', default=0)
    name = models.CharField('Заголовок блока', max_length=50)
    text = models.TextField('Текст блока')

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = 'Блок'
        verbose_name_plural = 'Блоки'


class Row(models.Model):
    name = models.CharField('Название', max_length=250, default='')
    text = models.TextField('Текст')

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = 'Строка'
        verbose_name_plural = 'Строки'


class Image(models.Model):
    name = models.CharField(max_length=100)
    path = models.ImageField()

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = 'Изображение'
        verbose_name_plural = 'Изображения'


class Table(models.Model):
    name = models.CharField('Название', max_length=250, default='')
    rows = models.ManyToManyField(Row)
    images = models.ManyToManyField(Image)

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = 'Таблица'
        verbose_name_plural = 'Таблицы'
