from uuid import uuid1
from django.db import models
from django.urls import reverse
from imagekit.models import ImageSpecField
from imagekit.processors import *
import mptt
from mptt.models import MPTTModel, TreeForeignKey
from core.models import Position, SEO


class Category(MPTTModel, SEO, Position):
    parent = TreeForeignKey('self', on_delete=models.SET_NULL, related_name='children',
                            null=True, blank=True, verbose_name='Родительская категория')
    title = models.CharField(max_length=250, unique=True, verbose_name='Название категории')
    desc = models.TextField(verbose_name='Описание', null=True, blank=True,)

    def get_absolute_url(self):
        return reverse('category', args=[self.slug])

    class Meta:
        verbose_name = 'Категория'
        verbose_name_plural = 'Категории'

    @property
    def sub_categories(self):
        return Category.objects.filter(parent=self)

    def __str__(self):
        return self.title
mptt.register(Category,)


class Product(SEO):
    category = models.ForeignKey(Category, on_delete=models.CASCADE, verbose_name='Категория', related_name='products')
    title = models.CharField(max_length=250, unique=True, verbose_name='Название товара')
    price = models.CharField(max_length=20, verbose_name='Цена', null=True, blank=True, help_text="Оставьте пустым и на сайте будет «под заказ»")
    desc = models.TextField(verbose_name='Описание')
    info = models.TextField(verbose_name='Характеристики', null=True, blank=True)
    is_active = models.BooleanField(default=True, verbose_name='Показывать на сайте')
    created = models.DateField(auto_now_add=True, verbose_name='Дата создания')
    updated = models.DateField(auto_now=True, verbose_name='Дата изменения')

    def get_absolute_url(self):
        return reverse('product', args=[self.category.slug, self.slug])

    class Meta:
        verbose_name = 'Товар'
        verbose_name_plural = 'Товары'
        ordering = ('created',)

    def __str__(self):
        return self.title

    def get_main_image(self):
        main_images = self.images.filter(is_main=True)
        if main_images.exists():
            main_image = main_images.first()
        else:
            main_image = self.images.first()
        return main_image


class Image(models.Model):
    product = models.ForeignKey(Product, on_delete=models.CASCADE, verbose_name='Товар', related_name='images')

    def get_picture_url(self, filename):
        ext = filename.split('.')[-1]
        filename = '{0}.{1}'.format(uuid1(), ext)
        return 'images/products/{0}'.format(filename)

    image = models.ImageField(upload_to=get_picture_url, verbose_name='Изображение')
    is_main = models.BooleanField(default=False, verbose_name='Главное изображение')

    image_medium = ImageSpecField(source='image',
                               processors=[ResizeToFit(524, 393)],
                               format='JPEG',
                               options={'quality': 90})
    
    image_small = ImageSpecField(source='image',
                               processors=[ResizeToFit(62, 62)],
                               format='JPEG',
                               options={'quality': 90})

    image_xxl = ImageSpecField(source='image',
                               processors=[ResizeToFit(1522, 1522)],
                               format='JPEG',
                               options={'quality': 90})

    image_big = ImageSpecField(source='image',
                               processors=[ResizeToFit(700, 700)],
                               format='JPEG',
                               options={'quality': 90})

    class Meta:
        verbose_name = 'Изображение'
        verbose_name_plural = 'Изображения'

    def __str__(self):
        return '{0}'.format(self.id)


class SimilarProduct(models.Model):
    product = models.ForeignKey(Product, on_delete=models.CASCADE, verbose_name='Товар', related_name='similars_for')
    similar_product = models.ForeignKey(Product, on_delete=models.CASCADE, verbose_name='Схожий товар', related_name='similars')

    class Meta:
        verbose_name = 'Товар'
        verbose_name_plural = 'С этим товаром смотрят'

    def __str__(self):
        return self.product.title