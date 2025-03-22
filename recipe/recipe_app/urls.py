from django.urls import path
from . import views

app_name = "recipe_app"



urlpatterns = [
    path('', views.home, name="home"),
    path('add_recipe/', views.add_recipe, name="add_recipe_with_form"),
    path('all_recipe/', views.all_recipe, name="recipes"),
]