from django.db import models

# Create your models here.
class employee(models.Model):
    id = models.IntegerField(primary_key=True)
    name = models.CharField(max_length=255)
    birthday = models.DateField()
    joining_date = models.DateField()
    email = models.EmailField(max_length=254)

class event(models.Model):
    name = models.CharField(max_length=100)
    repeat = models.CharField(max_length=50) 
    template = models.CharField(max_length=50)

class log(models.Model):
    date = models.DateField()
    log_message = models.CharField(max_length=255)