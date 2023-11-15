# Generated by Django 4.2 on 2023-11-15 13:12

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('oms', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='order',
            name='user',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='orders', to=settings.AUTH_USER_MODEL),
        ),
        migrations.AddField(
            model_name='itemvariationimage',
            name='item_variation',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='images', to='oms.itemvariation'),
        ),
        migrations.AddField(
            model_name='itemvariation',
            name='item',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='variations', to='oms.item'),
        ),
        migrations.AddField(
            model_name='itemvariation',
            name='variation_type',
            field=models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, related_name='variations', to='oms.variationtype'),
        ),
        migrations.AddField(
            model_name='itemimage',
            name='item',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='images', to='oms.item'),
        ),
        migrations.AddField(
            model_name='item',
            name='catagories',
            field=models.ManyToManyField(blank=True, to='oms.category'),
        ),
    ]
