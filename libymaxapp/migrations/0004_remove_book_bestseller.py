# Generated by Django 3.2.9 on 2021-12-05 16:13

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('libymaxapp', '0003_auto_20211205_1855'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='book',
            name='bestseller',
        ),
    ]
