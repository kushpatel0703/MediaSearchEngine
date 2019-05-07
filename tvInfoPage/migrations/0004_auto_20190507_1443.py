# Generated by Django 2.1.3 on 2019-05-07 19:43

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('tvInfoPage', '0003_auto_20190424_1957'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='watch_location',
            name='location_id',
        ),
        migrations.RemoveField(
            model_name='watch_location',
            name='tv_id',
        ),
        migrations.AddField(
            model_name='tv_details',
            name='country',
            field=models.CharField(default='none', max_length=200),
        ),
        migrations.AddField(
            model_name='tv_details',
            name='language',
            field=models.CharField(default='none', max_length=200),
        ),
        migrations.AddField(
            model_name='tv_details',
            name='year',
            field=models.CharField(default='none', max_length=200),
        ),
        migrations.AlterField(
            model_name='tv_details',
            name='description',
            field=models.TextField(default='none'),
        ),
        migrations.AlterField(
            model_name='tv_details',
            name='image_url',
            field=models.URLField(default='none'),
        ),
        migrations.AlterField(
            model_name='tv_details',
            name='imdb_id',
            field=models.CharField(default='none', max_length=200),
        ),
        migrations.AlterField(
            model_name='tv_details',
            name='imdb_rating',
            field=models.DecimalField(decimal_places=1, default='none', max_digits=2),
        ),
        migrations.AlterField(
            model_name='tv_details',
            name='title',
            field=models.CharField(default='none', max_length=200),
        ),
        migrations.DeleteModel(
            name='Locations',
        ),
        migrations.DeleteModel(
            name='Watch_location',
        ),
    ]
