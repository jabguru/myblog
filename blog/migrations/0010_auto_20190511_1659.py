# Generated by Django 2.1.8 on 2019-05-11 15:59

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0009_auto_20190511_1654'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='post',
            name='time',
        ),
        migrations.AlterField(
            model_name='post',
            name='published',
            field=models.DateTimeField(),
        ),
    ]