# Generated by Django 3.2.9 on 2021-12-05 13:10

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('libymaxapp', '0002_book_bestseller_books'),
    ]

    operations = [
        migrations.AddField(
            model_name='book',
            name='bestseller',
            field=models.BooleanField(default=False),
        ),
        migrations.AddField(
            model_name='book',
            name='recomended',
            field=models.BooleanField(default=False),
        ),
    ]
