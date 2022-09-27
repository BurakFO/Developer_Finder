from django.db import models

# Create your models here.
class Teacher(models.Model):
    name = models.CharField(max_length=80)
    age = models.IntegerField()


class Developer(models.Model):
    userName = models.CharField(max_length=20)
    location = models.CharField(max_length=20)
    followers = models.IntegerField()


class Test(models.Model):
    test = models.CharField(max_length=30)



