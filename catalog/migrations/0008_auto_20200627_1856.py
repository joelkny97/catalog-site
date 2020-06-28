# Generated by Django 2.2.10 on 2020-06-27 13:26

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('catalog', '0007_remove_book_published_year'),
    ]

    operations = [
        migrations.DeleteModel(
            name='AuthorPkAndSlug',
        ),
        migrations.AddField(
            model_name='author',
            name='slug',
            field=models.SlugField(default=django.utils.timezone.now, unique=True),
            preserve_default=False,
        ),
    ]
