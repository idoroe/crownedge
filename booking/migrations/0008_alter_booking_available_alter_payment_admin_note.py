# Generated by Django 4.0.3 on 2022-05-11 11:12

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('booking', '0007_payment_admin_note_payment_admin_update_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='booking',
            name='available',
            field=models.BooleanField(default=True),
        ),
        migrations.AlterField(
            model_name='payment',
            name='admin_note',
            field=models.TextField(blank=True, null=True),
        ),
    ]
