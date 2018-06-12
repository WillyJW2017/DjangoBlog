from django.db import models

# Create your models here.

class Article(models.Model):
    Title = models.CharField(max_length=32, default='Default Title')
    content = models.TextField(null=True)

    def __str__(self):
        return self.Title



