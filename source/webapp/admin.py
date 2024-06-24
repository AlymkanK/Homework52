from django.contrib import admin

from webapp.models import Task


class TaskAdmin(admin.ModelAdmin):
    list_display = ['id', 'description', 'status', 'due_date']
    list_display_links = ['id', 'description', 'status']
    list_filter = ['description']
    search_fields = ['description', 'status']
    fields = ['description', 'status', 'due_date']


admin.site.register(Task, TaskAdmin)
