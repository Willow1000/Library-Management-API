# Generated by Django 5.1.7 on 2025-03-13 09:16

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('books', '0002_book_ebook_available_book_physical_book_available'),
    ]

    operations = [
        migrations.AddField(
            model_name='physicalbookinventory',
            name='author',
            field=models.ForeignKey(default='', on_delete=django.db.models.deletion.CASCADE, to='books.author'),
        ),
    ]
