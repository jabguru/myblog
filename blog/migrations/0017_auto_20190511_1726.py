# Generated by Django 2.1.8 on 2019-05-11 16:26

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0016_auto_20190511_1724'),
    ]

    operations = [
        migrations.AlterField(
            model_name='post',
            name='featured_image',
            field=models.ImageField(null=True, upload_to='featured-images'),
        ),
    ]
