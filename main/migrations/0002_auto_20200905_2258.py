# Generated by Django 3.1.1 on 2020-09-05 22:58

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='urlmodel',
            name='clicks',
            field=models.IntegerField(null=True),
        ),
        migrations.AddField(
            model_name='urlmodel',
            name='slug',
            field=models.CharField(max_length=255, null=True),
        ),
    ]
