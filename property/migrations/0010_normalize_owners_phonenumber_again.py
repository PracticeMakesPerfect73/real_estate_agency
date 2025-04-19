# Generated by Django 5.2 on 2025-04-16 14:24

from django.db import migrations
import phonenumbers


def normalize_phone_numbers_again(apps, schema_editor):
    Flat = apps.get_model('property', 'Flat')

    for flat in Flat.objects.iterator():
        try:
            parsed = phonenumbers.parse(flat.owners_phonenumber, "RU")
            if phonenumbers.is_valid_number(parsed):
                flat.owner_pure_phone = phonenumbers.format_number(
                    parsed,
                    phonenumbers.PhoneNumberFormat.E164
                )
            else:
                flat.owner_pure_phone = 'unknown'
        except phonenumbers.NumberParseException:
            flat.owner_pure_phone = 'unknown'

        flat.save()


class Migration(migrations.Migration):

    dependencies = [
        ('property', '0009_alter_flat_owners_phonenumber'),
    ]

    operations = [
        migrations.RunPython(normalize_phone_numbers_again),
    ]
