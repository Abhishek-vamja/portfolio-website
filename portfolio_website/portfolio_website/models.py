from django.db import models


class Project(models.Model):
    title = models.CharField(max_length=255)
    language = models.CharField(max_length=255)
    framework = models.CharField(max_length=255)
    descriptions = models.TextField()
    url = models.URLField()