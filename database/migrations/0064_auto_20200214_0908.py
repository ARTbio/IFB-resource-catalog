# Generated by Django 3.0.3 on 2020-02-14 09:08

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('database', '0063_auto_20200213_1510'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='format',
            name='input',
        ),
        migrations.RemoveField(
            model_name='format',
            name='output',
        ),
        migrations.AddField(
            model_name='input',
            name='format',
            field=models.ManyToManyField(blank=True, to='database.Format'),
        ),
        migrations.AddField(
            model_name='output',
            name='format',
            field=models.ManyToManyField(blank=True, to='database.Format'),
        ),
    ]
