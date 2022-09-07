from django.db import models

# Create your models here.

class Author(models.Model):
    first_name = models.TextField(max_length=100)
    last_name = models.TextField(max_length=100)
    created_at = models.DateTimeField(auto_now_add=True)
    class Meta:
            ordering = ('-first_name',)

    def __str__(self):
        return self.first_name + self.last_name

    





class Book(models.Model):
    name = models.TextField(max_length=100)
    isbn = models.TextField(max_length=100)
    author = models.ForeignKey(Author, on_delete=models.CASCADE)
    created_at = models.DateTimeField(auto_now_add=True)

    class Meta:
            ordering = ('-name',)

    def __str__(self):
        return self.name


