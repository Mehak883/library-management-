# Generated by Django 4.1.7 on 2023-04-28 16:42

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('management', '0021_addbook_bookpic'),
    ]

    operations = [
        migrations.AlterField(
            model_name='addbook',
            name='bookpic',
            field=models.ImageField(blank=True, null=True, upload_to=''),
        ),
    ]
