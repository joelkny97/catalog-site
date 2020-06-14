# Generated by Django 2.2.10 on 2020-06-10 18:52

import catalog.models
import django.core.validators
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('catalog', '0003_auto_20200610_2311'),
    ]

    operations = [
        migrations.AddField(
            model_name='book',
            name='published_year',
            field=models.IntegerField(help_text='Enter published year for this book', null=True, validators=[django.core.validators.MinValueValidator(1000), catalog.models.max_year_current], verbose_name='published_year'),
        ),
    ]