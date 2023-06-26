# Generated by Django 4.2.1 on 2023-06-25 17:36

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('cart', '0002_bookincart_price'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='bookincart',
            name='price',
        ),
        migrations.AddField(
            model_name='order',
            name='price',
            field=models.DecimalField(decimal_places=2, default=0, max_digits=12),
        ),
    ]
