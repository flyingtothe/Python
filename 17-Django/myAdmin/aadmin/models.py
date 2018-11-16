from django.db import models
import time

# Create your models here.

class ClassRoom(models.Model):
    roomID = models.IntegerField()
    loc = models.CharField(max_length=20)
    roomName = models.CharField(max_length=20)

    def __str__(self):
        return self.roomName

class Teacher(models.Model):
    name = models.CharField(max_length=5)
    course = models.CharField(max_length=20)

    room = models.OneToOneField(ClassRoom, on_delete=models.CASCADE)

    # 关联对象
    def getRoomName(self):
        return self.room.roomName
    getRoomName.short_description = '教室'

    # 函数排序
    def curTime(self):
        return time.time()
    curTime.short_description = '当前时间'

    curTime.admin_order_field = 'name'

    def __str__(self):
        return self.name

class Student(models.Model):
    name = models.CharField(max_length=20)
    age = models.IntegerField()

    room = models.ForeignKey(ClassRoom, on_delete=models.CASCADE)

    def __str__(self):
        return self.name