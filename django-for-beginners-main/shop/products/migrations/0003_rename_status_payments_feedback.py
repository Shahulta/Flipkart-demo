# Generated by Django 4.2.2 on 2023-06-11 02:40

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('products', '0002_payments'),
    ]

    operations = [
        migrations.RenameField(
            model_name='payments',
            old_name='status',
            new_name='feedback',
        ),
    ]
