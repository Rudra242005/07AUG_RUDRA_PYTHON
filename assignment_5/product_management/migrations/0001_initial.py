# Generated by Django 5.0.1 on 2024-03-07 15:12

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='product_data',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('product_name', models.CharField(max_length=20)),
                ('product_model_name', models.CharField(max_length=20)),
                ('product_ram', models.CharField(max_length=20)),
                ('product_price', models.IntegerField()),
            ],
        ),
    ]
