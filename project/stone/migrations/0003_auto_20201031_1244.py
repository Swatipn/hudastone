# Generated by Django 3.1.1 on 2020-10-31 07:14

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('stone', '0002_posts'),
    ]

    operations = [
        migrations.AlterField(
            model_name='posts',
            name='content',
            field=models.TextField(max_length=50),
        ),
        migrations.AlterField(
            model_name='posts',
            name='title',
            field=models.CharField(max_length=50),
        ),
    ]
