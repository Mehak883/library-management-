# Generated by Django 4.1.7 on 2023-04-10 14:33

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('management', '0005_delete_addbook'),
    ]

    operations = [
        migrations.CreateModel(
            name='AddBook',
            fields=[
                ('bookid', models.CharField(max_length=10, primary_key=True, serialize=False)),
                ('bookname', models.CharField(max_length=50)),
                ('author', models.CharField(max_length=20)),
                ('category', models.CharField(max_length=10)),
            ],
        ),
    ]
