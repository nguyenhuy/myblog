from django.db import models

class Blog(models.Model):
    title = models.CharField(max_length=30)
    content = models.TextField()
    time_stamp = models.DateField()