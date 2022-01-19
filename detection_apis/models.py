from django.db import models


class Video(models.Model):
    link = models.CharField(max_length=200)


class VideoFile(models.Model):
    link = models.FileField()
