# Generated by Django 2.2 on 2021-09-15 06:38

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('abcompany', '0018_auto_20210915_1137'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='vacancymodel',
            name='slug',
        ),
    ]