# Generated by Django 4.1.3 on 2024-12-19 05:23

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('restaurant', '0012_restaurantuser_city_restaurantuser_place_and_more'),
    ]

    operations = [
        migrations.CreateModel(
            name='Restaurant',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
                ('address', models.CharField(default='Unknown Address', max_length=255)),
                ('phone_number', models.CharField(blank=True, max_length=15, null=True)),
                ('email', models.EmailField(blank=True, max_length=254, null=True)),
            ],
        ),
        migrations.RemoveField(
            model_name='restaurantuser',
            name='city',
        ),
        migrations.RemoveField(
            model_name='restaurantuser',
            name='place',
        ),
        migrations.RemoveField(
            model_name='restaurantuser',
            name='state',
        ),
        migrations.AddField(
            model_name='fooditems',
            name='is_out_of_stock',
            field=models.BooleanField(default=False),
        ),
    ]