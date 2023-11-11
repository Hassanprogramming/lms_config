from django.contrib import admin
from .models import ClassCategory, Classes

class ClassesAdmin(admin.ModelAdmin):
    filter_horizontal = ('img', 'video',)
    list_display = ['name', 'category']

admin.site.register(ClassCategory)
admin.site.register(Classes, ClassesAdmin)
