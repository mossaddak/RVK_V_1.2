# Generated by Django 4.1.7 on 2023-04-11 20:21

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('accounts', '0011_user_otp'),
    ]

    operations = [
        migrations.AlterField(
            model_name='user',
            name='city',
            field=models.CharField(blank=True, default=None, max_length=255, null=True),
        ),
    ]
