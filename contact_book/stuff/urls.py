from django.urls import path
from . import views

urlpatterns = [
    path('',views.home,name='home'),
    path('update/<int:id>/',views.update,name='update'),
    path('delete/<int:pk>/',views.delete,name='delete'),
]
