# Generated by Django 4.1.7 on 2023-04-11 18:26

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('about_prem_rawat', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='premrawattdescription',
            name='first_section_description',
            field=models.TextField(blank=True, null=True, verbose_name='First Section Description'),
        ),
        migrations.AlterField(
            model_name='premrawattdescription',
            name='fourth_section_description',
            field=models.TextField(blank=True, null=True, verbose_name='Third Section Description'),
        ),
        migrations.AlterField(
            model_name='premrawattdescription',
            name='second_section_description',
            field=models.TextField(blank=True, null=True, verbose_name='Second Section Description'),
        ),
        migrations.AlterField(
            model_name='premrawattdescription',
            name='thired_section_description',
            field=models.TextField(blank=True, null=True, verbose_name='Third Section Description'),
        ),
    ]