from django.db import models


class Address(models.Model):
    value = models.CharField(max_length=250, verbose_name='Адрес')

    class Meta:
        verbose_name = 'Адрес'
        verbose_name_plural = 'Адреса'

    def __str__(self):
        return self.value


class Phone(models.Model):
    value = models.CharField(max_length=20, verbose_name='Телефон')

    class Meta:
        verbose_name = 'Телефон'
        verbose_name_plural = 'Телефоны'

    def __str__(self):
        return self.value


class Email(models.Model):
    value = models.EmailField(max_length=250, verbose_name='E-mail')

    class Meta:
        verbose_name = 'E-mail'
        verbose_name_plural = 'E-mails'

    def __str__(self):
        return self.value


class MapCode(models.Model):
    value = models.TextField(verbose_name='Карта')

    class Meta:
        verbose_name = 'Карта'
        verbose_name_plural = 'Карты'

    def __str__(self):
        return self.value


class Schedule(models.Model):
    days = models.CharField(max_length=250, verbose_name='Дни недели')
    time = models.CharField(max_length=250, verbose_name='Время работы')

    class Meta:
        verbose_name = 'Пункт'
        verbose_name_plural = 'Режим работы'

    def __str__(self):
        return '{0} {1}'.format(self.days, self.time)


class Social(models.Model):
    name = models.CharField(max_length=250, verbose_name='Название социальной сети')
    short_name = models.CharField(max_length=250, verbose_name='Короткое название')
    link = models.URLField(max_length=250, verbose_name='Ссылка')

    class Meta:
        verbose_name = 'Социальная сеть'
        verbose_name_plural = 'Социальные сети'

    def __str__(self):
        return self.name


class WhatsApp(models.Model):
    value = models.CharField(max_length=20, verbose_name='Номер')

    class Meta:
        verbose_name = 'WhatsApp'
        verbose_name_plural = 'WhatsApp'

    def __str__(self):
        return self.value