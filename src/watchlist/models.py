from django.db import models


class Movie(models.Model):
    title = models.CharField(max_length=100)
    description = models.CharField(max_length=200)
    release_date = models.DateField()
    active = models.BooleanField(default=True)
    
    def __str__(self):
        return self.title