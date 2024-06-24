from django.urls import path

from webapp.views import add_task, view_tasks

urlpatterns = [
    path('add/', add_task),
    path('view/', view_tasks),
]
