# Generated by Django 2.2 on 2020-01-22 09:58

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('database', '0035_auto_20200122_0946'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='tool',
            name='link',
        ),
        migrations.DeleteModel(
            name='Link',
        ),
    ]
