# Generated by Django 3.2.9 on 2021-12-01 16:16

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0002_register'),
    ]

    operations = [
        migrations.AddField(
            model_name='register',
            name='role',
            field=models.CharField(default='', max_length=100),
        ),
    ]
