# Generated by Django 4.2.2 on 2023-06-11 03:03

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('products', '0005_delete_productname'),
    ]

    operations = [
        migrations.AlterField(
            model_name='payments',
            name='amount',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='products.product'),
        ),
    ]