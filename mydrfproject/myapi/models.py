from django.db import models

class Book(models.Model):
    title = models.CharField(max_length=300)
    author = models.CharField(max_length=500)
    published_date = models.DateTimeField()
    isbn = models.CharField(max_length=13 ,unique=True)
    page_count = models.IntegerField()
    langush = models.CharField( max_length=50, default='English')

    def __str__(self):
        return self.title