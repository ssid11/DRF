# Generated by Django 3.2.9 on 2021-11-22 10:55

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('todoapp', '0002_auto_20211122_1352'),
    ]

    operations = [
        migrations.AlterField(
            model_name='todo',
            name='project',
            field=models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to='todoapp.project', verbose_name='Название проекта'),
        ),
    ]