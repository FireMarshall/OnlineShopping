# Generated by Django 2.1.2 on 2019-05-03 06:34

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('shopping_app', '0010_auto_20190503_1203'),
    ]

    operations = [
        migrations.AlterField(
            model_name='product',
            name='date_added',
            field=models.DateTimeField(default=datetime.datetime(2019, 5, 3, 12, 4, 7, 923628)),
        ),
    ]