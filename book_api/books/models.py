
from django.db import models

class Book(models.Model):
    book_name = models.CharField(max_length=255)
    author = models.CharField(max_length=255)
    publisher = models.CharField(max_length=255)

    def __str__(self):
        return self.book_name
