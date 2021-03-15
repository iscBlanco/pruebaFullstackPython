from django.db import models

# Create your models here.
class SuperInformation(models.Model):
    id_superheroe   = models.IntegerField(primary_key=True)
    name            = models.CharField(max_length=100)
    alias           = models.CharField(max_length=100)
    age             = models.IntegerField(max_length=3)
    sex             = models.CharField(max_length=20)