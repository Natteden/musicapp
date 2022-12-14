# Generated by Django 4.1.3 on 2022-11-04 22:52

import datetime
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Artiste',
            fields=[
                ('Artiste_id', models.IntegerField(primary_key=True, serialize=False)),
                ('Firstname', models.CharField(max_length=20)),
                ('Lastname', models.CharField(max_length=20)),
            ],
        ),
        migrations.CreateModel(
            name='Song',
            fields=[
                ('title', models.CharField(max_length=50)),
                ('Datereleased', models.DateField(default=datetime.datetime.today)),
                ('Likes', models.CharField(max_length=1000)),
                ('Song_id', models.IntegerField(primary_key=True, serialize=False)),
                ('Artiste_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='polls.artiste')),
            ],
        ),
        migrations.CreateModel(
            name='Lyric',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('Content', models.CharField(max_length=1000)),
                ('Song_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='polls.song')),
            ],
        ),
    ]
