# Generated by Django 3.0.5 on 2020-06-23 18:21

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('orders', '0010_auto_20200622_2111'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='order',
            name='delivery',
        ),
    ]
