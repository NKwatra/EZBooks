# Generated by Django 2.2.4 on 2019-08-21 14:16

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('book', '0002_book_description'),
        ('order', '0001_initial'),
        ('user', '0004_auto_20190817_0448'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='customer',
            name='profile_pic',
        ),
        migrations.AddField(
            model_name='customer',
            name='orders',
            field=models.ManyToManyField(related_name='orders', through='order.Order', to='book.Book'),
        ),
        migrations.AlterField(
            model_name='customer',
            name='mobile_no',
            field=models.CharField(max_length=16, null=True),
        ),
    ]