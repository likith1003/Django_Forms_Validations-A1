from django.db import models

# Create your models here.

class Skool(models.Model):
    sname = models.CharField(max_length=50)
    princy = models.CharField(max_length=50)
    pno = models.CharField(max_length=50)
    add = models.CharField(max_length=50)

    def __str__(self):
        return self.sname