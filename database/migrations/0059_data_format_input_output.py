# Generated by Django 3.0.3 on 2020-02-12 13:06

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('database', '0058_operation'),
    ]

    operations = [
        migrations.CreateModel(
            name='Data',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('uri', models.TextField(blank=True, null=True)),
                ('term', models.TextField(blank=True, null=True)),
                ('additionDate', models.DateTimeField(auto_now_add=True)),
            ],
        ),
        migrations.CreateModel(
            name='Output',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('additionDate', models.DateTimeField(auto_now_add=True)),
                ('data', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, related_name='output', to='database.Data')),
                ('function', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='output', to='database.Function')),
            ],
        ),
        migrations.CreateModel(
            name='Input',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('additionDate', models.DateTimeField(auto_now_add=True)),
                ('data', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, related_name='input', to='database.Data')),
                ('function', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='input', to='database.Function')),
            ],
        ),
        migrations.CreateModel(
            name='Format',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('uri', models.TextField(blank=True, null=True)),
                ('term', models.TextField(blank=True, null=True)),
                ('additionDate', models.DateTimeField(auto_now_add=True)),
                ('input', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='format', to='database.Input')),
                ('output', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='format', to='database.Output')),
            ],
        ),
    ]