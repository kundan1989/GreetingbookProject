# Generated by Django 3.0.2 on 2020-03-15 18:33

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('socailmedia', '0002_auto_20200308_1908'),
    ]

    operations = [
        migrations.AlterField(
            model_name='postcomment',
            name='flag',
            field=models.CharField(blank=True, choices=[('racist', 'racist'), ('abusing', 'abusing')], max_length=20, null=True),
        ),
    ]
