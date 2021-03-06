# Generated by Django 2.2.2 on 2019-06-16 16:14

import datetime

from django.db import migrations, models
from django.utils.timezone import utc


class Migration(migrations.Migration):

    dependencies = [
        ('event', '0001_initial'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='event',
            options={'ordering': ['end_date'], 'verbose_name': 'Событие', 'verbose_name_plural': 'События'},
        ),
        migrations.AlterField(
            model_name='event',
            name='created',
            field=models.DateTimeField(default=datetime.datetime(2019, 6, 16, 16, 14, 24, 643991, tzinfo=utc), verbose_name='Время создания'),
        ),
    ]
