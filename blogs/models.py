from django.db import models

NULLABLE = {'blank': True, 'null': True}

class Blog(models.Model):
    title = models.CharField(max_length=100, verbose_name='Заголовок')
    content = models.TextField(verbose_name='Содержимое')
    image = models.ImageField(upload_to='main/', verbose_name='Изображение (превью)', **NULLABLE)
    create_data = models.DateField(verbose_name='Дата создания', **NULLABLE)

    is_published = models.BooleanField(default=True, verbose_name='Признак публикации', **NULLABLE)
    count_view = models.IntegerField(default=0, verbose_name='Количество просмотров')
    slug = models.CharField(max_length=150, verbose_name='slug', **NULLABLE)


    def __str__(self):
        return self.title

    class Meta:
        verbose_name = 'блог'
        verbose_name_plural = 'блоги'
