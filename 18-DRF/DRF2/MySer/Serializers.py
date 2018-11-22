# 序列化器包
from rest_framework import serializers

# 用来存放序列化器

class StudentSer(serializers.Serializer):
    '''
    包含每一个需要序列化/反序列化的字段
    与定义模型基本一致
    '''
    name = serializers.CharField(label='姓名', max_length=20)
    age = serializers.IntegerField()
    score = serializers.IntegerField()