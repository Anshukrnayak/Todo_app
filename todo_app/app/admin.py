from django.contrib import admin

from .models import TaskModel

# Register your models here.
@admin.register(TaskModel)
class TaskAdmin(admin.ModelAdmin):
    list_display=['name','description']

