# Generated by Django 4.2.2 on 2023-06-11 02:46

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('products', '0003_rename_status_payments_feedback'),
    ]

    operations = [
        migrations.CreateModel(
            name='ProductName',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('product_name', models.CharField(max_length=100)),
            ],
        ),
    ]
