from django.urls import path

from . import views

app_name = 'movie_collection_app'


urlpatterns = [
    path('', views.all_movies, name='all_movies'),
    path('create-movie/', views.create_movie, name='create_movie'),
    path('movie/<int:movie_id>/', views.movie_detail, name='movie_detail'),
    path('update_movie/<int:movie_pk>/', views.update_movie, name='update_movie'),
    path('confirm_delete_movie/<int:movie_id>/', views.confirm_delete, name='confirm_delete'),
    path('delete_movie/<int:movie_id>/', views.delete_movie, name='delete_movie'),
]