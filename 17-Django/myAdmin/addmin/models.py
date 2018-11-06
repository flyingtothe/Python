from django.db import models

# Create your models here.

class ClassRoom(models.Model):
    roomID = models.IntegerField()
    loc = models.CharField(max_length=20)
    roomName = models.CharField(max_length=20)

class Teacher(models.Model):
    name = models.CharField(max_length=5)
    course = models.CharField(max_length=20)
    room = models.OneToOneField(ClassRoom)

class Student(models.Model):
    name = models.CharField(max_length=5)
    age = models.IntegerField()
    room = models.OneToOneField(ClassRoom)

