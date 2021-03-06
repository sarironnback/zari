# Generated by Django 2.0.1 on 2018-02-27 14:19

import ckeditor.fields
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('pages', '0003_auto_20180205_1039'),
    ]

    operations = [
        migrations.AddField(
            model_name='creation',
            name='image',
            field=models.ImageField(default=1, upload_to='creation'),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='about',
            name='description',
            field=ckeditor.fields.RichTextField(),
        ),
        migrations.AlterField(
            model_name='creation',
            name='description',
            field=ckeditor.fields.RichTextField(),
        ),
    ]
