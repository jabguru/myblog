# Generated by Django 2.1.8 on 2019-05-23 00:11

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0042_auto_20190522_2204'),
    ]

    operations = [
        migrations.AlterField(
            model_name='post',
            name='featured_image',
            field=models.ImageField(blank=True, null=True, upload_to='featured-images/'),
        ),
    ]
