# Generated by Django 3.2.25 on 2024-06-02 09:41

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('marketplace', '0007_alter_game_sku'),
    ]

    operations = [
        migrations.AlterField(
            model_name='game',
            name='sku',
            field=models.CharField(blank=True, max_length=40, unique=True),
        ),
    ]
