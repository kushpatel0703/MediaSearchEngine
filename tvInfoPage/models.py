from django.db import models

class Genres(models.Model):
    genre = models.CharField(max_length=200)

    def __str__(self):
        return self.genre

class Locations(models.Model):
    location = models.CharField(max_length = 200)

    def __str__(self):
        return self.location

class Tv_details(models.Model):
    title = models.CharField(max_length = 200)
    imdb_id = models.CharField(max_length = 200)
    image_url = models.URLField(max_length = 200)
    description = models.TextField()
    imdb_rating = models.DecimalField(max_digits = 2, decimal_places = 1)

    def __str__(self):
        return self.title

class Watch_location(models.Model):
    tv_id = models.ForeignKey(Tv_details, on_delete = models.CASCADE)
    location_id = models.ForeignKey(Locations, on_delete = models.CASCADE)

    def __str__(self):
        return self.tv_id.title + " - " + self.location_id.location

class Tv_genre(models.Model):
    tv_id = models.ForeignKey(Tv_details, on_delete = models.CASCADE)
    genre_id = models.ForeignKey(Genres, on_delete = models.CASCADE)

    def __str__(self):
        return self.tv_id.title + " - " + self.genre_id.genre
