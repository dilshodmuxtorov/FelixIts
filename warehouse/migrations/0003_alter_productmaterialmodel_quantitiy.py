# Generated by Django 5.0.3 on 2024-03-16 18:36

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('warehouse', '0002_alter_warehousemodel_options_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='productmaterialmodel',
            name='quantitiy',
            field=models.FloatField(default=0),
        ),
    ]