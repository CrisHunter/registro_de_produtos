# Generated by Django 5.1.3 on 2024-11-24 01:52

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('produtos', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='produto',
            name='data_criacao',
        ),
        migrations.RemoveField(
            model_name='produto',
            name='quantidade',
        ),
    ]
