# Generated by Django 4.0.3 on 2022-04-13 10:47

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('room', '0008_alter_room_deluxe_suite_alter_room_luxury_suite_and_more'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='category',
            options={'managed': True, 'verbose_name': 'Category', 'verbose_name_plural': 'Categories'},
        ),
    ]
