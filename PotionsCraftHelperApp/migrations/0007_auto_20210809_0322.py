# Generated by Django 3.2.5 on 2021-08-09 00:22

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('PotionsCraftHelperApp', '0006_auto_20210808_2350'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='potion',
            name='explosive',
        ),
        migrations.RemoveField(
            model_name='potion',
            name='level',
        ),
        migrations.RemoveField(
            model_name='potion',
            name='lingering',
        ),
    ]
