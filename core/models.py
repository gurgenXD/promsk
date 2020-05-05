from django.db import models
from imagekit.models import ImageSpecField
from imagekit.processors import ResizeToFit, ResizeToFill
from contacts.models import Phone


class SEO(models.Model):
    seo_title = models.CharField(max_length=250, verbose_name='Title', null=True, blank=True)
    seo_desc = models.CharField(max_length=250, verbose_name='Description', null=True, blank=True)
    seo_kwrds = models.CharField(max_length=250, verbose_name='Keywords', blank=True)
    slug = models.SlugField(max_length=250, verbose_name='Slug', unique=True)

    class Meta:
        abstract = True


class Position(models.Model):
    position = models.PositiveIntegerField(verbose_name='Позиция', null=True, blank=True)

    def save(self, *args, **kwargs):
        if self.position is None:
            try:
                last = self.objects.order_by('-position')[0]
                self.position = last.position + 1
            except:
                self.position = 0
        return super(Position, self).save(*args, **kwargs)

    class Meta:
        abstract = True
        ordering = ('position',)


class MailToString(models.Model):
    email = models.EmailField(max_length=250, verbose_name='E-mail')

    class Meta:
        verbose_name = 'Кому отправлять письмо'
        verbose_name_plural = 'Кому отправлять письмо'

    def __str__(self):
        return self.email


class MailFromString(models.Model):
    use_tls = models.BooleanField(verbose_name='EMAIL_USE_TLS(gmail.com, mail.ru)')
    use_ssl = models.BooleanField(verbose_name='EMAIL_USE_SSL(yandex.ru)')
    port = models.PositiveIntegerField(verbose_name='EMAIL_PORT')
    host = models.CharField(max_length=250, verbose_name='EMAIL_HOST')
    host_user = models.EmailField(max_length=250, verbose_name='EMAIL_HOST_USER')
    host_password = models.CharField(max_length=250, verbose_name='EMAIL_HOST_PASSWORD')

    class Meta:
        verbose_name = 'Откуда отправлять письмо'
        verbose_name_plural = 'Откуда отправлять письмо'

    def __str__(self):
        return self.host_user


class TitleTag(models.Model):
    url = models.CharField(max_length=250, verbose_name='URL')
    seo_title = models.CharField(max_length=250, verbose_name='Title', null=True, blank=True)
    seo_desc = models.CharField(max_length=250, verbose_name='Description', null=True, blank=True)
    seo_kwrds = models.CharField(max_length=250, verbose_name='Keywords', null=True, blank=True)

    class Meta:
        verbose_name = 'SEO title'
        verbose_name_plural = 'SEO titles'

    def __str__(self):
        return self.seo_title


class Index(models.Model):
    title = models.CharField(max_length=250, verbose_name='Заголовок')
    title_text = models.TextField(verbose_name='Текст под заголовком')
    about = models.TextField(verbose_name='О нас')
    phone1 = models.ForeignKey(Phone, on_delete=models.CASCADE, related_name='index1', verbose_name='Телефон в меню', null=True, blank=True)
    phone2 = models.ForeignKey(Phone, on_delete=models.CASCADE, related_name='index2', verbose_name='Телефон в меню', null=True, blank=True)

    class Meta:
        verbose_name = 'Статические элементы'
        verbose_name_plural = 'Статические элементы'

    def __str__(self):
        return 'Статические элементы №{0}'.format(self.id)


class ProductInIndex(models.Model):
    index = models.ForeignKey(Index, on_delete=models.CASCADE, verbose_name='Статические элементы', related_name='index_products')
    product = models.ForeignKey('products.Product', on_delete=models.CASCADE, verbose_name='Товар', related_name='index_products')

    class Meta:
        verbose_name = 'Популярный товар'
        verbose_name_plural = 'Популярные товары'


class CategoryInIndex(models.Model):
    index = models.ForeignKey(Index, on_delete=models.CASCADE, verbose_name='Статические элементы', related_name='index_categories')
    category = models.ForeignKey('products.Category', on_delete=models.CASCADE, verbose_name='Категория', related_name='index_categories')
    image = models.ImageField(upload_to='index_products/', verbose_name='Изображение')
    image_small = ImageSpecField(source='image',
                               processors=[ResizeToFill(526, 296)],
                               format='JPEG',
                               options={'quality': 90})

    class Meta:
        verbose_name = 'Категория'
        verbose_name_plural = 'Категории'


class Proc(models.Model):
    index = models.ForeignKey(Index, on_delete=models.CASCADE, verbose_name='Главная', related_name='procs')
    title = models.CharField(max_length=250, verbose_name='Заголовок')
    text = models.TextField(verbose_name='Описание')
    image = models.FileField(upload_to='index/procs/', max_length=254, verbose_name='Изображение')

    class Meta:
        verbose_name = 'Преимущество'
        verbose_name_plural = 'Преимущества'

    def __str__(self):
        return self.title


