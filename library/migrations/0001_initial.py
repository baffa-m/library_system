# Generated by Django 4.1.3 on 2022-12-09 08:04

import datetime
from django.db import migrations, models
import django.db.models.deletion
import uuid


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Books',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=200, unique=True)),
                ('author', models.CharField(max_length=200)),
                ('isbn', models.IntegerField()),
                ('date_received', models.DateTimeField(default=datetime.datetime.utcnow)),
            ],
        ),
        migrations.CreateModel(
            name='Categories',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('category', models.CharField(max_length=200, unique=True)),
            ],
        ),
        migrations.CreateModel(
            name='BookInstance',
            fields=[
                ('id', models.UUIDField(default=uuid.uuid4, primary_key=True, serialize=False)),
                ('due_back', models.DateField(null=True)),
                ('status', models.CharField(choices=[('m', 'maintenance'), ('r', 'Reserved'), ('c', 'Checked Out'), ('a', 'Available')], default='a', max_length=1)),
                ('book', models.ForeignKey(on_delete=django.db.models.deletion.RESTRICT, to='library.books')),
            ],
            options={
                'ordering': ['due_back'],
            },
        ),
    ]
