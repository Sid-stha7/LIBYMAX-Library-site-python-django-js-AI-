# Generated by Django 3.2.9 on 2021-12-05 17:25

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('libymaxapp', '0006_booksearch'),
    ]

    operations = [
        migrations.CreateModel(
            name='Data',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('book_title', models.CharField(max_length=100)),
                ('book_author', models.CharField(max_length=100)),
                ('book_genre', models.CharField(max_length=100)),
            ],
        ),
        migrations.DeleteModel(
            name='BookSearch',
        ),
    ]
