# Generated by Django 2.1.8 on 2019-05-23 01:02

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0044_auto_20190523_0142'),
    ]

    operations = [
        migrations.AlterField(
            model_name='featured_post',
            name='post',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='featured', to='blog.Post'),
        ),
    ]
