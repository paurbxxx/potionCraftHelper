# Generated by Django 3.2.5 on 2021-08-11 22:30

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('PotionsCraftHelperApp', '0009_auto_20210810_1553'),
    ]

    operations = [
        migrations.AlterField(
            model_name='potion',
            name='time',
            field=models.CharField(max_length=15, null=True),
        ),
        migrations.AlterField(
            model_name='potion',
            name='time_plus',
            field=models.CharField(blank=True, max_length=15, null=True),
        ),
        migrations.AlterField(
            model_name='potion',
            name='time_up_level',
            field=models.CharField(blank=True, max_length=15, null=True),
        ),
    ]
