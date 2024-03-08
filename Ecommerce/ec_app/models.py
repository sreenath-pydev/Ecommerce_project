from django.db import models

# Create your models here.
class SetSettings(models.Model):
    banner = models.ImageField(upload_to='media/site')
    caption = models.TextField()
