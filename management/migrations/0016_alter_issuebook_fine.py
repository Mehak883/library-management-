# Generated by Django 4.1.7 on 2023-04-13 04:44

from django.db import migrations, models
import management.models


class Migration(migrations.Migration):

    dependencies = [
        ('management', '0015_alter_issuebook_fine'),
    ]

    operations = [
        migrations.AlterField(
            model_name='issuebook',
            name='fine',
            field=models.IntegerField(default=management.models.finey),
        ),
    ]
