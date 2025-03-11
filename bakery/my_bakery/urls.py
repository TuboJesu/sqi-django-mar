from django.urls import path

from . import views

app_name = "my_bakery"


urlpatterns = [
    path('', views.homepage, name="homepage"),
    path('about-us/', views.aboutpage, name="aboutpage"),
    path('contact-us/', views.contactpage, name="contactpage"),
    path('menu', views.menupage, name="menupage"),
]

