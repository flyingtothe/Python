from django.contrib import admin
from aadmin.models import Student, Teacher, ClassRoom

# Register your models here.

admin.site.site_header = '头'
admin.site.site_title = '标题'
admin.site.index_title = '首页标语'

# 在 admin.site 中进行注册
# admin.site.register(Student)
# admin.site.register(Teacher)
# admin.site.register(ClassRoom)


# 每个模型定义一套管理类
@admin.register(ClassRoom)
class ClassRoomAdmin(admin.ModelAdmin):
    pass

class TeacherAdmin(admin.ModelAdmin):
    list_per_page = 2
    actions_on_bottom = True
    actions_on_top = False
    list_display = ['name', 'room', 'curTime', 'getRoomName']
    # 搜索栏
    search_fields = ['name']

    # 控制界面显示字段
    # fields = ['name', 'course']

    # 分组
    fieldsets = (
        ('基本信息', {'fields':['name',]}),
        ('其他信息', {'fields':['room', 'course']}),
    )

class StudentAdmin(admin.ModelAdmin):
    pass

admin.site.register(Student, ClassRoomAdmin)
admin.site.register(Teacher, TeacherAdmin)
# admin.site.register(ClassRoom, StudentAdmin)