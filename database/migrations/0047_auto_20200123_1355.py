# Generated by Django 2.2 on 2020-01-23 13:55

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('database', '0046_auto_20200123_1329'),
    ]

    operations = [
        migrations.CreateModel(
            name='ElixirNode',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('elixirNode', models.TextField(null=True)),
                ('additionDate', models.DateTimeField(auto_now_add=True)),
            ],
        ),
        migrations.CreateModel(
            name='ElixirPlatform',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('elixirPlatform', models.TextField(null=True)),
                ('additionDate', models.DateTimeField(auto_now_add=True)),
            ],
        ),
        migrations.RemoveField(
            model_name='tool',
            name='elixirNode',
        ),
        migrations.RemoveField(
            model_name='tool',
            name='elixirPlatform',
        ),
        migrations.AddField(
            model_name='tool',
            name='additionDate',
            field=models.DateTimeField(blank=True, null=True),
        ),
        migrations.AddField(
            model_name='tool',
            name='lastUpdate',
            field=models.DateTimeField(auto_now=True),
        ),
        migrations.AddField(
            model_name='tool',
            name='elixir_node',
            field=models.ManyToManyField(blank=True, to='database.ElixirNode'),
        ),
        migrations.AddField(
            model_name='tool',
            name='elixir_platform',
            field=models.ManyToManyField(blank=True, to='database.ElixirPlatform'),
        ),
    ]
