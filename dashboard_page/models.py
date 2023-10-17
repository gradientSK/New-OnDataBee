from django.db import models

# Create your models here.

class youtube_id(models.Model):
    channelid = models.CharField(max_length=100)
