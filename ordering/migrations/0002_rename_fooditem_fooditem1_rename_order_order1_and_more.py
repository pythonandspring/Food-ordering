# Generated by Django 4.1.3 on 2024-11-10 11:45

from django.conf import settings
from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('ordering', '0001_initial'),
    ]

    operations = [
        migrations.RenameModel(
            old_name='FoodItem',
            new_name='FoodItem1',
        ),
        migrations.RenameModel(
            old_name='Order',
            new_name='Order1',
        ),
        migrations.RenameModel(
            old_name='OrderItem',
            new_name='OrderItem1',
        ),
    ]