# Generated by Django 4.0.3 on 2022-04-13 10:56

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0004_companyprofile_favicon'),
    ]

    operations = [
        migrations.AddField(
            model_name='talktous',
            name='admin_note',
            field=models.TextField(default='a'),
        ),
        migrations.AddField(
            model_name='talktous',
            name='cleared',
            field=models.DateField(auto_now=True),
        ),
        migrations.AddField(
            model_name='talktous',
            name='created',
            field=models.DateField(auto_now=True),
        ),
        migrations.AddField(
            model_name='talktous',
            name='status',
            field=models.CharField(choices=[('New', 'New'), ('Processing', 'Processing'), ('Cleared', 'Cleared')], default='New', max_length=50),
        ),
    ]
