# Generated by Django 5.2.1 on 2025-05-25 09:11

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('product', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='product',
            name='category',
            field=models.CharField(choices=[('computer', 'Computers'), ('food', 'Food'), ('kids', 'Kids')], max_length=30),
        ),
    ]
