# Generated by Django 2.2.10 on 2020-06-28 18:52

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('catalog', '0016_remove_book_published_year'),
    ]

    operations = [
        migrations.AddField(
            model_name='book',
            name='slug',
            field=models.SlugField(allow_unicode=True, blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='author',
            name='slug',
            field=models.SlugField(allow_unicode=True, blank=True, unique=True),
        ),
    ]
