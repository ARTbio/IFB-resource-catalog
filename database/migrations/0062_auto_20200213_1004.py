# Generated by Django 3.0.3 on 2020-02-13 10:04

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('database', '0061_auto_20200213_0959'),
    ]

    operations = [
        migrations.CreateModel(
            name='TypeRole',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(blank=True, max_length=100, null=True)),
                ('additionDate', models.DateTimeField(auto_now_add=True)),
            ],
        ),
        migrations.RemoveField(
            model_name='toolcredit',
            name='typeRole',
        ),
        migrations.AddField(
            model_name='toolcredit',
            name='typeRole',
            field=models.ManyToManyField(blank=True, to='database.TypeRole'),
        ),
    ]
