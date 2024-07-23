from django.urls import path
from . import views

urlpatterns = [
    path('',views.home,name = 'home'),
    path('completed/',views.completed,name='complete'),
    path('Remaining/',views.remaining,name='remaining'),
    path('add_task/',views.add_task,name='add_task'),
    path('delete_task/<int:pk>/',views.delete_task,name='delete'),
    path('task_details/<int:pk>/',views.task_details,name = 'task_details'),
    path('clicked/<int:pk>/',views.click_complete,name = 'clicked'),
]
