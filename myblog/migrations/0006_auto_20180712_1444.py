# Generated by Django 2.0.6 on 2018-07-12 14:44

from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        ('myblog', '0005_auto_20180712_1434'),
    ]

    operations = [
        migrations.AlterField(
            model_name='category',
            name='name',
            field=models.CharField(max_length=100, verbose_name='分类'),
        ),
        migrations.AlterField(
            model_name='post',
            name='created_time',
            field=models.DateTimeField(verbose_name='创建时间'),
        ),
        migrations.AlterField(
            model_name='post',
            name='excerpt',
            field=models.CharField(blank=True, max_length=200, verbose_name='摘要'),
        ),
        migrations.AlterField(
            model_name='post',
            name='modified_time',
            field=models.DateTimeField(verbose_name='修改时间'),
        ),
        migrations.AlterField(
            model_name='post',
            name='title',
            field=models.CharField(max_length=70, verbose_name='标题'),
        ),
        migrations.AlterField(
            model_name='post',
            name='views',
            field=models.PositiveIntegerField(default=0, verbose_name='阅读数'),
        ),
        migrations.AlterField(
            model_name='tag',
            name='name',
            field=models.CharField(max_length=100, verbose_name='标签'),
        ),
    ]
