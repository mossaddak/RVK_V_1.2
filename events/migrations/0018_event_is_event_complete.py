# Generated by Django 4.1.7 on 2023-04-08 15:54

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('events', '0017_eventregisteruser_amount'),
    ]

    operations = [
        migrations.AddField(
            model_name='event',
            name='is_event_complete',
            field=models.BooleanField(null=True, verbose_name='Is event completed?'),
        ),
    ]
