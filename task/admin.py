from django.contrib import admin

# Register your models here.
from task.models import Task, Solution


class TaskAdmin(admin.ModelAdmin):
    model = Task


class SolutionAdmin(admin.ModelAdmin):
    model = Solution


admin.site.register(Task, TaskAdmin)
admin.site.register(Solution, TaskAdmin)
