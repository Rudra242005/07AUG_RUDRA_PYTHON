from django.db import models

# Create your models here.

class coustomer(models.Model):
    firstname=models.CharField(max_length=20)
    lastname=models.CharField(max_length=20)
    username=models.EmailField()
    password=models.CharField(max_length=10)
    city=models.CharField(max_length=20)
    state=models.CharField(max_length=20)
    zip=models.IntegerField()
    mobile=models.BigIntegerField()


class contact(models.Model):
    name = models.CharField(max_length=20)
    email = models.EmailField()
    mobile = models.BigIntegerField()
    text = models.TextField()