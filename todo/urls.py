from django.urls import path
from . import views

app_name = 'todo'
urlpatterns = [
    path('', views.index, name='index'),
    path('addTask', views.addTask, name='addTask'),
    path('<int:id>deleteTask', views.deleteTask, name='deleteTask'),
    path('<int:id>updateTask', views.updateTask, name='updateTask'),
]