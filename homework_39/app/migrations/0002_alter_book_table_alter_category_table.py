# Generated by Django 5.1.2 on 2024-11-09 18:37

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0001_initial'),
    ]

    operations = [
        migrations.AlterModelTable(
            name='book',
            table='Book',
        ),
        migrations.AlterModelTable(
            name='category',
            table='Category',
        ),
    ]
