# Generated by Django 2.2 on 2020-01-21 13:48

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('database', '0017_auto_20200121_1346'),
    ]

    operations = [
        migrations.AddField(
            model_name='tool',
            name='function',
            field=models.CharField(blank=True, max_length=1000, null=True),
        ),
    ]