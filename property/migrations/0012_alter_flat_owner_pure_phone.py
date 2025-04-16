# Generated by Django 5.2 on 2025-04-16 14:47

import phonenumber_field.modelfields
from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('property', '0011_owner'),
    ]

    operations = [
        migrations.AlterField(
            model_name='flat',
            name='owner_pure_phone',
            field=phonenumber_field.modelfields.PhoneNumberField(blank=True, db_index=True, help_text='Нормализованный номер владельца', max_length=128, null=True, region='RU', verbose_name='Нормализованный номер владельца'),
        ),
    ]
