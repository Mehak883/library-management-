# Generated by Django 4.1.7 on 2023-04-29 06:18

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('management', '0026_remove_issuebook_bookpic'),
    ]

    operations = [
        migrations.AlterField(
            model_name='addbook',
            name='bookpic',
            field=models.ImageField(blank=True, default=None, null=True, upload_to=''),
        ),
    ]
