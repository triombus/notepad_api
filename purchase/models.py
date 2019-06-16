from django.db import models


class Purchase(models.Model):
    name = models.CharField(verbose_name='Название покупки', max_length=128)

    class Meta:
        verbose_name = 'Покупка'
        verbose_name_plural = 'Покупки'
        ordering = ['-id']

    def __str__(self):
        return self.name


class PurchaseItem(models.Model):
    purchase = models.ForeignKey(Purchase, verbose_name='Покупка', on_delete=models.CASCADE)
    name = models.CharField(verbose_name='Название продукта / предмета', max_length=128)
    is_buy = models.BooleanField(verbose_name='Куплено', default=False)

    class Meta:
        verbose_name = 'Список продуктов / предметов'
        verbose_name_plural = 'Списки продуктов / предметов'
        ordering = ['name']

    def __str__(self):
        return self.name