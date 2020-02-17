# Generated by Django 3.0.3 on 2020-02-12 10:20

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('database', '0052_auto_20200207_1320'),
    ]

    operations = [
        migrations.CreateModel(
            name='Link',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('url', models.CharField(blank=True, max_length=200, null=True)),
                ('type', models.CharField(blank=True, max_length=100, null=True)),
                ('note', models.CharField(blank=True, max_length=1000, null=True)),
                ('additionDate', models.DateTimeField(auto_now_add=True)),
                ('tool_id', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='link', to='database.Tool')),
            ],
        ),
    ]
