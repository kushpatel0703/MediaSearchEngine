# Generated by Django 2.1.3 on 2019-04-24 22:57

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('tvInfoPage', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='tv_details',
            name='rotten_tomatoes_audeince',
        ),
        migrations.RemoveField(
            model_name='tv_details',
            name='rotten_tomatoes_critic',
        ),
    ]
