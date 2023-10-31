# Generated by Django 4.1.5 on 2023-09-20 17:32

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0002_alter_verificationcode_code'),
    ]

    operations = [
        migrations.AddField(
            model_name='settings',
            name='usd_npr_exchange_rate',
            field=models.DecimalField(decimal_places=2, default=135.0, max_digits=60),
        ),
        migrations.AlterField(
            model_name='verificationcode',
            name='code',
            field=models.CharField(default=955004, max_length=6),
        ),
    ]
