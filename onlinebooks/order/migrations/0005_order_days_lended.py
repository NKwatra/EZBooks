# Generated by Django 2.2.4 on 2019-08-22 02:50

import django.core.validators
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('order', '0004_remove_order_days_lended'),
    ]

    operations = [
        migrations.AddField(
            model_name='order',
            name='days_lended',
            field=models.IntegerField(blank=True, null=True, validators=[django.core.validators.MinValueValidator(7), django.core.validators.MaxValueValidator(21)]),
        ),
    ]
