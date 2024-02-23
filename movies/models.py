from django.db import models

# Create your models here.
class Movie(models.Model):
    year=models.IntegerField()
    movie_name=models.CharField(max_length=100)
    genre=models.CharField(max_length=100)
    image=models.URLField()


    def __str__(self):
        return self.title
