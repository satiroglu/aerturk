# Generated by Django 4.1.1 on 2022-09-16 00:27

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('pages', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='page',
            name='location',
            field=models.CharField(choices=[('0', 'Navbar'), ('1', 'Footer')], default='0', max_length=1, verbose_name='Menü Konumu'),
        ),
    ]
