from rest_framework import serializers
from case01.models import *

# 序列化器文件
class StudentSer(serializers.ModelSerializer):
    class Meta:
        model = Student
        fields = '__all__'