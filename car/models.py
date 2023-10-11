from django.db import models

# Create your models here.
from django.db import models

class Car(models.Model):

    model = models.CharField(max_length=25)
    price = models.FloatField()
