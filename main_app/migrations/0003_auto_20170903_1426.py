# -*- coding: utf-8 -*-
# Generated by Django 1.11.4 on 2017-09-03 11:26
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('main_app', '0002_auto_20170830_2141'),
    ]

    operations = [
        migrations.CreateModel(
            name='Persons',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=128)),
                ('surname', models.CharField(max_length=128)),
                ('middlename', models.CharField(max_length=128)),
                ('age', models.IntegerField()),
            ],
        ),
        migrations.CreateModel(
            name='Sex',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=20)),
            ],
        ),
        migrations.RenameModel(
            old_name='workplaces',
            new_name='Learning_places',
        ),
        migrations.RenameModel(
            old_name='learningplaces',
            new_name='Work_places',
        ),
        migrations.DeleteModel(
            name='person',
        ),
        migrations.CreateModel(
            name='Politic',
            fields=[
                ('person', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, primary_key=True, serialize=False, to='main_app.Persons')),
                ('political_party', models.CharField(max_length=256)),
                ('political_philosophy', models.CharField(max_length=256)),
            ],
        ),
        migrations.AddField(
            model_name='persons',
            name='children',
            field=models.ManyToManyField(related_name='_persons_children_+', to='main_app.Persons'),
        ),
        migrations.AddField(
            model_name='persons',
            name='hobbies',
            field=models.ManyToManyField(to='main_app.Hobbies'),
        ),
        migrations.AddField(
            model_name='persons',
            name='learning_places',
            field=models.ManyToManyField(to='main_app.Learning_places'),
        ),
        migrations.AddField(
            model_name='persons',
            name='sex',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='main_app.Sex'),
        ),
        migrations.AddField(
            model_name='persons',
            name='work_places',
            field=models.ManyToManyField(to='main_app.Work_places'),
        ),
    ]