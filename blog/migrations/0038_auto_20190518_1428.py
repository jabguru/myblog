# Generated by Django 2.1.8 on 2019-05-18 13:28

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0037_auto_20190518_1408'),
    ]

    operations = [
        migrations.RenameField(
            model_name='comment',
            old_name='author',
            new_name='name',
        ),
    ]
