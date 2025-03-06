from django.urls import path

from . import views

urlpatterns = [

    path('home/', views.homepage, name="home"),
    path('tasks/', views.all_tasks, name="tasks"),

]