# Generated by Django 2.2.10 on 2020-06-14 17:39

from django.db import migrations


class Migration(migrations.Migration):
    dependencies = [
        ('catalog', '0006_auto_20200614_2306'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='book',
            name='published_year',
        ),
    ]
