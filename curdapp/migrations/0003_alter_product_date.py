# Generated by Django 4.1.1 on 2022-11-20 07:11

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('curdapp', '0002_alter_product_date'),
    ]

    operations = [
        migrations.AlterField(
            model_name='product',
            name='date',
            field=models.DateTimeField(auto_now_add=True),
        ),
    ]
