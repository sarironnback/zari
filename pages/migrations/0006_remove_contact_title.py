# Generated by Django 2.0.1 on 2018-10-28 22:54

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('pages', '0005_auto_20180227_1526'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='contact',
            name='title',
        ),
    ]
