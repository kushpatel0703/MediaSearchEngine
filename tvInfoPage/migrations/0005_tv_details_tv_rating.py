# Generated by Django 2.1.3 on 2019-05-07 19:46

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('tvInfoPage', '0004_auto_20190507_1443'),
    ]

    operations = [
        migrations.AddField(
            model_name='tv_details',
            name='tv_rating',
            field=models.CharField(default='none', max_length=200),
        ),
    ]