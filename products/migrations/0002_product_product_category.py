# Generated by Django 3.2.9 on 2021-11-04 00:47

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('products', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='product',
            name='product_category',
            field=models.CharField(blank=True, choices=[('B', 'Barato'), ('M', 'Médio'), ('C', 'Caro')], max_length=10, null=True),
        ),
    ]
