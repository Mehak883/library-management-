# Generated by Django 4.1.7 on 2023-03-29 13:47

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Register',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('emailid', models.CharField(max_length=200)),
                ('password', models.CharField(max_length=200)),
                ('mobile', models.CharField(max_length=200)),
                ('fullname', models.CharField(max_length=200)),
            ],
        ),
    ]
