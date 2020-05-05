from django.db import models


class Order(models.Model):
    name = models.CharField(max_length=250, verbose_name='Имя')
    email = models.EmailField(max_length=250, verbose_name='Электронная почта')
    phone = models.CharField(max_length=20, verbose_name='Телефон')
    product = models.ForeignKey('products.Product', on_delete=models.CASCADE, related_name='orders', verbose_name='Товар')
    text = models.TextField(verbose_name='Описание заказа')
    created = models.DateTimeField(auto_now_add=True, verbose_name='Время заявки')

    class Meta:
        verbose_name = 'Заказ'
        verbose_name_plural = 'Заказы'

    def __str__(self):
        return '{0} ({1}, {2})'.format(self.name, self.email, self.phone)