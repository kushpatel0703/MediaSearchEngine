# Generated by Django 2.1.3 on 2019-04-24 22:35

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Genres',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('genre', models.CharField(max_length=200)),
            ],
        ),
        migrations.CreateModel(
            name='Locations',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('location', models.CharField(max_length=200)),
            ],
        ),
        migrations.CreateModel(
            name='Movie_genre',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('genre_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='tvInfoPage.Genres')),
            ],
        ),
        migrations.CreateModel(
            name='Tv_details',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=200)),
                ('imdb_id', models.CharField(max_length=200)),
                ('image_url', models.URLField()),
                ('description', models.TextField()),
                ('rotten_tomatoes_critic', models.IntegerField()),
                ('rotten_tomatoes_audeince', models.IntegerField()),
                ('imdb_rating', models.DecimalField(decimal_places=1, max_digits=2)),
            ],
        ),
        migrations.CreateModel(
            name='Watch_location',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('location_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='tvInfoPage.Locations')),
                ('tv_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='tvInfoPage.Tv_details')),
            ],
        ),
        migrations.AddField(
            model_name='movie_genre',
            name='tv_id',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='tvInfoPage.Tv_details'),
        ),
    ]