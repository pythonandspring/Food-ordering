# Generated by Django 5.1.4 on 2024-12-24 15:35

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('restaurant', '0014_restaurantuser_city_restaurantuser_place_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='restaurantuser',
            name='place',
            field=models.CharField(max_length=50),
        ),
    ]
