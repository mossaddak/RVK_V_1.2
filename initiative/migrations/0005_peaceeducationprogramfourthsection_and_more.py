# Generated by Django 4.1.7 on 2023-04-10 14:37

import ckeditor_uploader.fields
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('initiative', '0004_peaceeducationprogramthiredsection'),
    ]

    operations = [
        migrations.CreateModel(
            name='PeaceEducationProgramFourthSection',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('desc', ckeditor_uploader.fields.RichTextUploadingField(blank=True, null=True, verbose_name='Description')),
                ('image', models.ImageField(blank=True, null=True, upload_to='')),
            ],
            options={
                'verbose_name_plural': 'Peace Education Program Fourth Section',
            },
        ),
        migrations.AlterModelOptions(
            name='peaceeducationprogramsecondsection',
            options={'verbose_name_plural': 'Peace Education Program Second Section'},
        ),
        migrations.AlterModelOptions(
            name='peaceeducationprogramthiredsection',
            options={'verbose_name_plural': 'Peace Education Program Third Section'},
        ),
        migrations.AlterModelOptions(
            name='peaceeducationprogramtopsection',
            options={'verbose_name_plural': 'Peace Education Program First Section'},
        ),
    ]
