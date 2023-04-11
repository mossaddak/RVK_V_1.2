# Generated by Django 4.1.7 on 2023-04-09 13:47

import ckeditor_uploader.fields
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('news', '0005_alter_news_options'),
    ]

    operations = [
        migrations.AddField(
            model_name='news',
            name='details',
            field=ckeditor_uploader.fields.RichTextUploadingField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='news',
            name='image',
            field=models.ImageField(null=True, upload_to=''),
        ),
    ]
