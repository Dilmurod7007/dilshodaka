# Generated by Django 2.2 on 2021-10-19 18:38

from django.db import migrations, models
import pagesstatic.models


class Migration(migrations.Migration):

    dependencies = [
        ('pagesstatic', '0003_auto_20210831_1204'),
    ]

    operations = [
        migrations.CreateModel(
            name='PageTitleModel',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(blank=True, max_length=150, null=True)),
                ('page_promo', models.FileField(blank=True, null=True, upload_to=pagesstatic.models.upload_location)),
                ('image', models.ImageField(blank=True, null=True, upload_to=pagesstatic.models.upload_location)),
            ],
            options={
                'verbose_name': 'Page Title',
                'verbose_name_plural': 'Page Title',
            },
        ),
    ]
