# Generated by Django 2.2.4 on 2019-08-29 08:13

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('shop', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='product',
            name='dosage',
            field=models.CharField(default='', max_length=20),
        ),
        migrations.AddField(
            model_name='product',
            name='size',
            field=models.CharField(default='', max_length=20),
        ),
        migrations.AlterField(
            model_name='product',
            name='brand',
            field=models.CharField(default='', max_length=50),
        ),
    ]
