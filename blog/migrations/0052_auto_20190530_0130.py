# Generated by Django 2.1.8 on 2019-05-30 00:30

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0051_auto_20190530_0126'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='userprofile',
            name='user',
        ),
        migrations.DeleteModel(
            name='UserProfile',
        ),
    ]