# Generated by Django 5.1.2 on 2024-12-02 17:47

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0004_book_stock'),
    ]

    operations = [
        migrations.AddField(
            model_name='book',
            name='price',
            field=models.DecimalField(decimal_places=2, default=30, max_digits=10),
            preserve_default=False,
        ),
    ]
