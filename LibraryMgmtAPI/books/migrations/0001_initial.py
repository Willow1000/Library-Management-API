# Generated by Django 5.1.7 on 2025-03-10 14:22

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Author',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=50)),
                ('biography', models.TextField()),
            ],
        ),
        migrations.CreateModel(
            name='BookUser',
            fields=[
                ('name', models.CharField(max_length=200)),
                ('member_no', models.AutoField(primary_key=True, serialize=False)),
            ],
        ),
        migrations.CreateModel(
            name='PhysicalBookInventory',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=50)),
                ('location', models.CharField(max_length=50)),
            ],
        ),
        migrations.CreateModel(
            name='Book',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=50)),
                ('author', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='books.author')),
            ],
            options={
                'constraints': [models.UniqueConstraint(fields=('title', 'author'), name='unique_book_title_author')],
            },
        ),
        migrations.CreateModel(
            name='EBook',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=200)),
                ('pages', models.IntegerField()),
                ('publication_date', models.DateField()),
                ('size', models.PositiveIntegerField()),
                ('file_format', models.CharField(max_length=50)),
                ('download_link', models.URLField()),
                ('author', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='ebooks', to='books.author')),
            ],
            options={
                'constraints': [models.UniqueConstraint(fields=('title', 'author'), name='unique_ebook_title_author')],
            },
        ),
        migrations.CreateModel(
            name='PhysicalBook',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=200)),
                ('pages', models.IntegerField()),
                ('publication_date', models.DateField()),
                ('location', models.CharField(max_length=200)),
                ('isbn', models.IntegerField(unique=True)),
                ('available', models.BooleanField(default=True)),
                ('author', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='books', to='books.author')),
            ],
            options={
                'constraints': [models.UniqueConstraint(fields=('isbn',), name='unique_isbn')],
            },
        ),
        migrations.CreateModel(
            name='PhysicalBookPublic',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=200)),
                ('pages', models.IntegerField()),
                ('publication_date', models.DateField()),
                ('author', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='public_physical_books', to='books.author')),
            ],
            options={
                'constraints': [models.UniqueConstraint(fields=('title', 'author'), name='public_physical_book_unique_title_author')],
            },
        ),
    ]
