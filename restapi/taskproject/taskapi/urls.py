from django.urls import path
from .views import TaskListCreate, TaskRetrieveUpdateDelete

urlpatterns = [
    path('tasks/', TaskListCreate.as_view(), name='task-list-create'),
    path('tasks/<int:pk>/', TaskRetrieveUpdateDelete.as_view(), name='task-retrieve-update-delete'),
]
