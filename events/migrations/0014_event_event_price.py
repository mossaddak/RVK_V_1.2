# Generated by Django 4.1.7 on 2023-04-08 10:26

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('events', '0013_eventregisteruser_address_eventregisteruser_city_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='event',
            name='event_price',
            field=models.CharField(max_length=250, null=True, verbose_name='Event Price'),
        ),
    ]
