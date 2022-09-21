from django.db import models

# Create your models here.
class Post(models.Model):
    fullName = models.CharField(max_length=100)
    date = models.TextField(blank=True)
    fullUrl = models.TextField(blank=True)
    comment = models.TextField(blank=True)
