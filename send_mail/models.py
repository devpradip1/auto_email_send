from django.db import models

# Create your models here.
class employee(models.Model):
    name = models.CharField(max_length=100)
    email = models.EmailField(max_length=50)
    birth_date = models.DateField()
    anniversary_date =models.DateField()
    