# Generated by Django 2.2.2 on 2019-06-16 14:52

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Purchase',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=128, verbose_name='Название покупки')),
            ],
            options={
                'verbose_name': 'Покупка',
                'verbose_name_plural': 'Покупки',
                'ordering': ['-id'],
            },
        ),
        migrations.CreateModel(
            name='PurchaseItem',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=128, verbose_name='Название продукта / предмета')),
                ('is_buy', models.BooleanField(default=False, verbose_name='Куплено')),
                ('purchase', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='purchase.Purchase', verbose_name='Покупка')),
            ],
            options={
                'verbose_name': 'Список продуктов / предметов',
                'verbose_name_plural': 'Списки продуктов / предметов',
                'ordering': ['name'],
            },
        ),
    ]
