# Generated by Django 4.2 on 2023-11-14 14:29

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='userbase',
            name='first_name',
            field=models.CharField(blank=True, default='', max_length=150),
        ),
        migrations.AlterField(
            model_name='userbase',
            name='last_name',
            field=models.CharField(blank=True, default='', max_length=150),
        ),
    ]
