# Generated by Django 2.2 on 2021-09-07 08:38

from django.db import migrations, models
import portfolio.models


class Migration(migrations.Migration):

    dependencies = [
        ('portfolio', '0004_auto_20210906_1717'),
    ]

    operations = [
        migrations.AddField(
            model_name='pagetitlemodel',
            name='image',
            field=models.ImageField(blank=True, null=True, upload_to=portfolio.models.upload_location),
        ),
    ]