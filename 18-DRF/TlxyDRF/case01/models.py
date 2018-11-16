from django.db import models

# Create your models here.

class ClassRoom(models.Model):
    loc = models.CharField(max_length=20)
    roomName = models.CharField(max_length=20)

class Teacher(models.Model):
    name = models.CharField(max_length=5)
    course = models.CharField(max_length=20)
    age = models.IntegerField()

class Student(models.Model):
    name = models.CharField(max_length=20)
    age = models.IntegerField()
