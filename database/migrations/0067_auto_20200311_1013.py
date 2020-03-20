# Generated by Django 3.0.4 on 2020-03-11 10:13

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('database', '0066_download'),
    ]

    operations = [
        migrations.CreateModel(
            name='PublicationMetadata',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('updated', models.DateTimeField(blank=True, null=True)),
                ('title', models.TextField(blank=True, null=True)),
                ('journal', models.TextField(blank=True, null=True)),
                ('abstract', models.TextField(blank=True, null=True)),
                ('date', models.DateTimeField(blank=True, null=True)),
                ('citationCount', models.IntegerField(default=0)),
            ],
        ),
        migrations.CreateModel(
            name='PublicationAuthor',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.TextField(blank=True, null=True)),
                ('metadata', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='authors', to='database.PublicationMetadata')),
            ],
        ),
        migrations.AddField(
            model_name='publication',
            name='metadata',
            field=models.OneToOneField(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='publication', to='database.PublicationMetadata'),
        ),
    ]
