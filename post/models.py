from autoslug import AutoSlugField
from ckeditor.fields import RichTextField
from django.db import models


class Author(models.Model):
    author_name = models.CharField(max_length=100)
    author_email = models.EmailField()

    def __str__(self):
        return self.author_email


class Blog(models.Model):
    title = models.CharField(max_length=100)
    post = RichTextField()
    slug = AutoSlugField(populate_from='title')
    author = models.ForeignKey(Author, on_delete=models.CASCADE)
    created_date = models.DateField(auto_now_add=True)
    updated_date = models.DateField(auto_now=True)

    def __str__(self):
        return self.author.author_email
