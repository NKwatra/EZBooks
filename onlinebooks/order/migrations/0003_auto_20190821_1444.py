# Generated by Django 2.2.4 on 2019-08-21 14:44

import django.core.validators
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('order', '0002_auto_20190821_1428'),
    ]

    operations = [
        migrations.AlterField(
            model_name='order',
            name='days_lended',
            field=models.IntegerField(blank=True, null=True, validators=[django.core.validators.MinValueValidator(0), django.core.validators.MaxValueValidator(21)]),
        ),
    ]
