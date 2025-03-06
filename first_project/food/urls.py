from django.urls import path

from . import views


urlpatterns = [

    path('our-menu/', views.menu, name="menu"),
    path('contact-us/', views.contact, name="contact")
]