# Generated by Django 4.2.2 on 2023-06-11 04:22

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('products', '0010_rename_payments_buy'),
    ]

    operations = [
        migrations.RenameModel(
            old_name='Buy',
            new_name='Booking',
        ),
    ]