# Generated by Django 4.2.1 on 2023-07-08 19:23

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('cart', '0010_cart_contact_phone'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='cart',
            name='contact_phone',
        ),
        migrations.AddField(
            model_name='cart',
            name='phone',
            field=models.CharField(blank=True, default=None, max_length=15, null=True),
        ),
    ]