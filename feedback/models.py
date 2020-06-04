from django.db import models
import datetime

# Create your models here.
class Feedback(models.Model):
    name = models.CharField(max_length = 100)
    email = models.EmailField()
    comment = models.TextField()
    createDate = models.DateField()
    