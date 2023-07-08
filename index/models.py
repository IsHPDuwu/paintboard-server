from django.db import models

# Create your models here.


class Tokenlist(models.Model):
    token = models.CharField(max_length=100)
    time = models.IntegerField(default=0)
