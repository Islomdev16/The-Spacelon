from django.db import models
from django.utils import timezone
from django.contrib.auth.models import User

class Project(models.Model):
    title = models.CharField(max_length=200)
    image = models.ImageField(upload_to='pics')
    text = models.TextField()
    date_posted = models.DateTimeField(default=timezone.now)


    def __str__(self):
        return self.title

class Blog(models.Model):
    title = models.CharField(max_length=200)
    image = models.ImageField(upload_to='pics')
    date_posted = models.DateTimeField(default=timezone.now)
    text = models.TextField()

    def __str__(self):
        return self.title
        


