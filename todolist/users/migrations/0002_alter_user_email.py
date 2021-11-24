# Generated by Django 3.2.9 on 2021-11-22 10:35

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='user',
            name='email',
            field=models.EmailField(help_text='Обязательное поле. Должно быть уникальным', max_length=254, unique=True, verbose_name='Адрес электронной почты'),
        ),
    ]
