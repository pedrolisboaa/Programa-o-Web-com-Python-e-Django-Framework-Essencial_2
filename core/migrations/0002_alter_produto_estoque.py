# Generated by Django 4.1.7 on 2023-03-19 03:16

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='produto',
            name='estoque',
            field=models.IntegerField(max_length=10, verbose_name='Estoque'),
        ),
    ]
