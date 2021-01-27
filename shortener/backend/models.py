
from django.db import models
from django.contrib.auth.models import User


class Shortener(models.Model):
    uid         = models.AutoField(primary_key=True)
    slug        = models.SlugField(max_length=11, unique=True)
    url         = models.URLField(max_length=1000, unique=False)
    date        = models.DateTimeField(auto_now=True)

    def __str__(self):
        return "slug:/{} for url:{}".format(self.slug, self.url)

