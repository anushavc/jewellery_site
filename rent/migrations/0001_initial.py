# Generated by Django 3.1.2 on 2020-11-11 18:05

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='jewellery',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('groupid', models.IntegerField()),
                ('name', models.CharField(max_length=200)),
                ('description', models.CharField(max_length=500)),
                ('category', models.CharField(max_length=100)),
                ('rental_price', models.IntegerField()),
                ('retail_price', models.IntegerField()),
                ('image', models.ImageField(upload_to='photos', verbose_name='jewellery_name')),
            ],
        ),
        migrations.CreateModel(
            name='group',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('productid', models.IntegerField()),
                ('groupid', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='rent.jewellery')),
            ],
        ),
    ]