from django.db import models


class Blog(models.Model):
    title = models.CharField(max_length=30)
    content = models.TextField()
    time_stamp = models.DateField()
    version = models.IntegerField(default=0)

    @classmethod
    def exists(cls, blog_id):
        return len(cls.objects.filter(id=blog_id)) > 0