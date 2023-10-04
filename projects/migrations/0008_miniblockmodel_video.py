# Generated by Django 2.2 on 2022-02-28 12:22

import django.core.validators
from django.db import migrations, models
import projects.models


class Migration(migrations.Migration):

    dependencies = [
        ('projects', '0007_pagetitlemodel_image'),
    ]

    operations = [
        migrations.AddField(
            model_name='miniblockmodel',
            name='video',
            field=models.FileField(blank=True, null=True, upload_to=projects.models.upload_location, validators=[django.core.validators.FileExtensionValidator(allowed_extensions=['MOV', 'avi', 'mp4', 'webm', 'mkv'])]),
        ),
    ]