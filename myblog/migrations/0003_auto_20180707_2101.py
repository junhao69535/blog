# Generated by Django 2.0.6 on 2018-07-07 13:01

from django.db import migrations


class Migration(migrations.Migration):
    dependencies = [
        ('myblog', '0002_auto_20180707_2019'),
    ]

    operations = [
        migrations.RenameField(
            model_name='post',
            old_name='titile',
            new_name='title',
        ),
    ]
