# Generated by Django 2.0.1 on 2018-02-05 09:39

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('pages', '0002_auto_20180205_1038'),
    ]

    operations = [
        migrations.AlterField(
            model_name='about',
            name='description',
            field=models.TextField(),
        ),
        migrations.AlterField(
            model_name='contact',
            name='message',
            field=models.TextField(),
        ),
    ]
