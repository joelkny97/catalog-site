# Generated by Django 2.2.10 on 2020-06-10 19:17

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('catalog', '0004_book_published_year'),
    ]

    operations = [
        migrations.AddField(
            model_name='book',
            name='published_date',
            field=models.DateField(blank=True, help_text='Enter published date for this book', null=True, verbose_name='Published Date'),
        ),
    ]