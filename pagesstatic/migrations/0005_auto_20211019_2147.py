# Generated by Django 2.2 on 2021-10-19 18:47

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('pagesstatic', '0004_pagetitlemodel'),
    ]

    operations = [
        migrations.RenameModel(
            old_name='PageTitleModel',
            new_name='BannerModel',
        ),
        migrations.AlterModelOptions(
            name='bannermodel',
            options={'verbose_name': 'Page banner', 'verbose_name_plural': 'Page banner'},
        ),
    ]
