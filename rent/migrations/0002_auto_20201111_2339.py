# Generated by Django 3.1.2 on 2020-11-11 18:09

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('rent', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='jewellery',
            name='image',
            field=models.CharField(max_length=300),
        ),
    ]