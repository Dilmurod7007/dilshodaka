# Generated by Django 2.2 on 2022-02-28 12:22

import abcompany.models
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('abcompany', '0029_auto_20211030_1904'),
    ]

    operations = [
        migrations.AlterField(
            model_name='aboutusmodel',
            name='image',
            field=models.ImageField(blank=True, null=True, upload_to=abcompany.models.upload_location),
        ),
    ]
