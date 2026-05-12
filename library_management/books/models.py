from django.db import models

class Book(models.Model):
    name = models.CharField(max_length=100)
    author = models.CharField(max_length=100)
    publisher = models.CharField(max_length=100)
    category = models.CharField(max_length=100)
    av_cpy = models.IntegerField()
    pub_year = models.DateField()
    def __str__(self):
        return self.name





