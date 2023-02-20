from django.db import models


# Create your models here.
class place(models.Model):
    name = models.CharField(max_length=250)
    img = models.ImageField(upload_to='pics')
    description = models.TextField(max_length=2500)


class ourteam(models.Model):
    img1 = models.ImageField(upload_to='pics')
    name1 = models.CharField(max_length=250)
    description1 = models.TextField(max_length=2500)
