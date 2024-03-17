from django.db import models

# Create your models here.


class SimpleModel(models.Model):
    SimpleText = models.CharField(max_length=100)
