# Generated by Django 4.2 on 2023-11-12 03:48

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('tenants', '0002_alter_client_type'),
    ]

    operations = [
        migrations.AlterField(
            model_name='client',
            name='type',
            field=models.CharField(choices=[('public', 'public'), ('oms', 'oms'), ('ecommerce', 'ecommerce')], max_length=100),
        ),
    ]
