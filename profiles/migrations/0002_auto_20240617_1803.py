# Generated by Django 3.2.25 on 2024-06-17 18:03

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('marketplace', '0001_initial'),
        ('profiles', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='userprofile',
            name='default_town_or_city',
            field=models.CharField(blank=True, max_length=25, null=True),
        ),
        migrations.AlterField(
            model_name='userprofile',
            name='games_for_sale',
            field=models.ManyToManyField(blank=True, related_name='games_for_sale_by_user', to='marketplace.Game'),
        ),
        migrations.AlterField(
            model_name='userprofile',
            name='games_owned',
            field=models.ManyToManyField(blank=True, related_name='games_owned_by_user', to='marketplace.Game'),
        ),
    ]
