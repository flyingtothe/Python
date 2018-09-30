from django.db import models

# Create your models here.
class Teacher(models.Model):

    name = models.CharField(max_length=12)  # 字符串
    age = models.IntegerField()
    address = models.CharField(max_length=50)
    course = models.CharField(max_length=25)

    def __str__(self):
        return self.name

class School(models.Model):
    school_id = models.IntegerField()
    school_name = models.CharField(max_length=20)

    my_manager = models.OneToOneField('Teacher', on_delete=models.CASCADE)

    def __str__(self):
        return self.school_name