# Generated by Django 2.2 on 2020-01-21 11:55

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('database', '0006_auto_20200121_1147'),
    ]

    operations = [
        migrations.AddField(
            model_name='tool',
            name='language',
            field=models.CharField(blank=True, max_length=1000, null=True),
        ),
    ]