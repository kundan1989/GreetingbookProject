# Generated by Django 3.0.2 on 2020-03-08 13:38

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('socailmedia', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='mypost',
            name='pic',
            field=models.ImageField(null=True, upload_to='images'),
        ),
        migrations.AlterField(
            model_name='myprofile',
            name='pic',
            field=models.ImageField(null=True, upload_to='images'),
        ),
    ]
