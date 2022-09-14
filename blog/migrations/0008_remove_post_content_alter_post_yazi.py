# Generated by Django 4.1.1 on 2022-09-14 23:01

from django.db import migrations
import tinymce.models


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0007_post_yazi'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='post',
            name='content',
        ),
        migrations.AlterField(
            model_name='post',
            name='yazi',
            field=tinymce.models.HTMLField(verbose_name='Yazı'),
        ),
    ]