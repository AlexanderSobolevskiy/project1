# Generated by Django 3.0.5 on 2020-06-22 18:11

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('orders', '0009_delivery'),
    ]

    operations = [
        migrations.AddField(
            model_name='order',
            name='delivery',
            field=models.BooleanField(default=False),
        ),
        migrations.DeleteModel(
            name='Delivery',
        ),
    ]
