# Generated by Django 3.2.25 on 2024-06-01 12:49

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('marketplace', '0003_auto_20240525_1311'),
    ]

    operations = [
        migrations.AlterField(
            model_name='game',
            name='condition',
            field=models.CharField(choices=[('as_new', 'As new'), ('great', 'Great'), ('good', 'Good'), ('fair', 'Fair'), ('signs_of_time', 'Signs of time'), ('heavily_used', 'Heavily used')], max_length=15),
        ),
    ]