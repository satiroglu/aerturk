# Generated by Django 4.1.1 on 2022-09-14 22:14

from django.db import migrations
import tinymce.models


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0006_comment'),
    ]

    operations = [
        migrations.AddField(
            model_name='post',
            name='yazi',
            field=tinymce.models.HTMLField(default=1),
            preserve_default=False,
        ),
    ]
