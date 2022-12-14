# Generated by Django 4.1.1 on 2022-09-06 22:55

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('utilisateur', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Attente',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=300)),
                ('num', models.CharField(max_length=300)),
                ('longi', models.CharField(max_length=300)),
                ('lati', models.CharField(max_length=300)),
                ('jour', models.DateTimeField(auto_now=True)),
            ],
            options={
                'ordering': ['-jour'],
            },
        ),
        migrations.CreateModel(
            name='Fini',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=300)),
                ('num', models.CharField(max_length=300)),
                ('longi', models.CharField(max_length=300)),
                ('lati', models.CharField(max_length=300)),
                ('jour', models.DateTimeField(auto_now=True)),
                ('fini', models.BooleanField(default=False)),
                ('fait_par', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]
