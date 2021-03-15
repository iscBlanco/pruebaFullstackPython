from django.db import models
from django.core.validators import MaxValueValidator

# Create your models here.
class SuperInformation(models.Model):
    id_superheroe   = models.AutoField(primary_key=True)
    name            = models.CharField(max_length=100)
    alias           = models.CharField(max_length=100)
    age             = models.PositiveIntegerField(validators=[MaxValueValidator(99)])
    sex             = models.CharField(max_length=20)