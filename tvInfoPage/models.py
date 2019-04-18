from django.db import models

class Genres(models.Model):
    genre = models.CharField(max_length=200)

class Locations(models.Model):
    location = models.CharField(max_length = 200)

class Tv_details(models.Model):
    title = models.CharField(max_length = 200)
    image_url = models.URLField(max_length = 200)
    description = models.TextField()
    rotten_tomatoes_critic = models.IntegerField()
    rotten_tomatoes_audeince = models.IntegerField()
    imdb_rating = models.DecimalField(max_digits = 2, decimal_places = 1)

class Watch_location(models.Model):
    tv_id = models.ForeignKey(Tv_details, on_delete = models.CASCADE)
    location_id = models.ForeignKey(Locations, on_delete = models.CASCADE)

class Movie_genre(models.Model):
    tv_id = models.ForeignKey(Tv_details, on_delete = models.CASCADE)
    genre_id = models.ForeignKey(Genres, on_delete = models.CASCADE)
