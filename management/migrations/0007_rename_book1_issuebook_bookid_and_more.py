# Generated by Django 4.1.7 on 2023-04-12 13:45

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('management', '0006_addbook'),
    ]

    operations = [
        migrations.RenameField(
            model_name='issuebook',
            old_name='book1',
            new_name='bookid',
        ),
        migrations.RemoveField(
            model_name='issuebook',
            name='studentid',
        ),
    ]
