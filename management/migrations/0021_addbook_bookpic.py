# Generated by Django 4.1.7 on 2023-04-28 16:35

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('management', '0020_bookreturn'),
    ]

    operations = [
        migrations.AddField(
            model_name='addbook',
            name='bookpic',
            field=models.ImageField(default=None, height_field=50, upload_to=None, width_field=50),
        ),
    ]
