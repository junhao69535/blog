# Generated by Django 2.0.6 on 2018-07-09 02:58

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('myblog', '0003_auto_20180707_2101'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='post',
            options={'ordering': ['-created_time']},
        ),
        migrations.AddField(
            model_name='post',
            name='views',
            field=models.PositiveIntegerField(default=0),
        ),
    ]