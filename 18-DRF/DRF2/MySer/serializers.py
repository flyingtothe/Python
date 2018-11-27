# 序列化器包
from rest_framework import serializers
from MySer.models import Student

# 用来存放序列化器

# class StudentSer(serializers.Serializer):
# 超链接版
class StudentSer(serializers.HyperlinkedModelSerializer):
    '''
    包含每一个需要序列化/反序列化的字段
    与定义模型基本一致
    '''
    # name = serializers.CharField(label='姓名', max_length=20)
    # age = serializers.IntegerField()
    # score = serializers.IntegerField()

    class Meta:
        # 告诉序列化器，对应哪个模型
        model = Student

        # fields = ('name', 'age', 'score')
        fields = '__all__'