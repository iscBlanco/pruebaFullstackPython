from django.db import models
from superinfo.models import SuperInformation

# Create your models here.
class SuperPowersModel(models.Model):
    id_superpowers  = models.AutoField(primary_key=True)
    description     = models.CharField(max_length=200)
    superheroe      = models.ForeignKey(SuperInformation, on_delete=models.CASCADE)
