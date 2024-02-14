from django.db import models

# Create your models here.


class BookModel(models.Model):
    book_name = models.CharField(max_length=64)
    book_author = models.CharField(max_length=64)
    book_img = models.ImageField(upload_to='book_images')