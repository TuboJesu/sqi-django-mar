from django.urls import path

from . import views

App_name = "quotes"

urlpatterns = [
    path('quotes/', views.get_quotes, name="quotes"),
]