from django.contrib import admin
from .models import *

class ClassesAdmin(admin.ModelAdmin):
    filter_horizontal = ('img', 'video',)
    list_display = ['name', 'category']


class CourseAdmin(admin.ModelAdmin):
    list_display = ['name', 'student', 'time_added']
    filter_horizontal = ['classes']
    list_filter = ('name', 'student', 'time_added')
    

admin.site.register(ClassCategory)
admin.site.register(Classes, ClassesAdmin)
admin.site.register(VideoClass)
admin.site.register(ImageClass)
admin.site.register(VideoCategory)