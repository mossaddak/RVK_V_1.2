# Generated by Django 4.1.7 on 2023-04-12 13:32

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('events', '0031_alter_event_options_alter_event_event_price'),
    ]

    operations = [
        migrations.AlterField(
            model_name='event',
            name='event_price',
            field=models.CharField(blank=True, default=None, max_length=250, null=True, verbose_name='Event Price'),
        ),
    ]