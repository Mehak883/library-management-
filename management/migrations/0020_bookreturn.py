# Generated by Django 4.1.7 on 2023-04-22 16:29

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('management', '0019_delete_returnbook'),
    ]

    operations = [
        migrations.CreateModel(
            name='BookReturn',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('studentuser', models.CharField(blank=True, max_length=100)),
                ('bookname', models.CharField(blank=True, max_length=20)),
                ('stuname', models.CharField(blank=True, max_length=20)),
                ('bookid', models.CharField(max_length=20)),
                ('issuedate', models.DateField()),
                ('expirydate', models.DateField()),
                ('fine', models.IntegerField()),
                ('returndate', models.DateField(auto_now=True)),
            ],
        ),
    ]