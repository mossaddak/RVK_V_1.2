# Generated by Django 4.1.7 on 2023-04-09 15:54

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0005_remove_initiative_details'),
    ]

    operations = [
        migrations.CreateModel(
            name='NewsShelter',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('email', models.EmailField(max_length=254)),
            ],
            options={
                'verbose_name_plural': 'News Shelter',
            },
        ),
    ]
