# Generated by Django 3.2.25 on 2024-06-20 10:02

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('marketplace', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='game',
            name='image',
            field=models.ImageField(blank=True, upload_to='game_images/'),
        ),
    ]
