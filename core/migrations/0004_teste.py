# Generated by Django 4.1.7 on 2023-03-19 03:19

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0003_alter_produto_estoque'),
    ]

    operations = [
        migrations.CreateModel(
            name='Teste',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('teste', models.CharField(max_length=10, verbose_name='Nome')),
            ],
        ),
    ]
