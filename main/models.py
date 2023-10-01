from django.db import models

NULLABLE = {'blank': True, 'null': True}

class Category(models.Model):
    name = models.CharField(max_length=100, verbose_name='Наименование')
    description = models.TextField(verbose_name='Описание')

    def __str__(self):
        return f'{self.name}({self.description})'

    class Meta:
        verbose_name = 'категория'
        verbose_name_plural = 'категории'

class Product(models.Model):
    name = models.CharField(max_length=100, verbose_name='Наименование')
    description = models.TextField(verbose_name='Описание')
    image = models.ImageField(upload_to='main/',verbose_name='изображение (превью)', **NULLABLE)
    category = models.ForeignKey(Category, on_delete=models.CASCADE, verbose_name='Категория')
    cost = models.DecimalField(max_digits=10, decimal_places=2, verbose_name='Цена за покупку')
    create_data = models.DateTimeField(verbose_name='Дата создания', **NULLABLE)
    change_data = models.DateTimeField(verbose_name='Дата последнего изменения', **NULLABLE)

    def __str__(self):
        return f'{self.name}({self.description}, {self.category}, {self.cost})'

    class Meta:
        verbose_name = 'продукт'
        verbose_name_plural = 'продукты'

class Version(models.Model):
    version_number = models.IntegerField(verbose_name='Номер версии', unique=True)
    version_name = models.CharField(max_length=100, verbose_name='Название версии')
    product = models.ForeignKey(Product, on_delete=models.CASCADE, verbose_name='Продукт')


    is_active = models.BooleanField(default=True, verbose_name='Активная версия')


    def __str__(self):
        return f'{self.version_number} ({self.product}, {self.version_name})'

    class Meta:
        verbose_name = 'версию'
        verbose_name_plural = 'версии'