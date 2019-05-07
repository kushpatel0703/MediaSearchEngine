from django.db import models

class Genres(models.Model):
    genre = models.CharField(max_length=200)

    def __str__(self):
        return self.genre

class Tv_details(models.Model):
    title = models.CharField(max_length = 200, default = "none")
    year = models.CharField(max_length = 200, default = "none")
    country = models.CharField(max_length = 200, default = "none")
    language = models.CharField(max_length = 200, default = "none")
    imdb_id = models.CharField(max_length = 200, default = "none")
    image_url = models.URLField(max_length = 200, default = "none")
    description = models.TextField(default = "none")
    tv_rating = models.CharField(max_length = 200, default = "none")
    imdb_rating = models.DecimalField(max_digits = 2, decimal_places = 1, default = "none")

    def __str__(self):
        return self.title

class Tv_genre(models.Model):
    tv_id = models.ForeignKey(Tv_details, on_delete = models.CASCADE)
    genre_id = models.ForeignKey(Genres, on_delete = models.CASCADE)

    def __str__(self):
        return self.tv_id.title + " - " + self.genre_id.genre
