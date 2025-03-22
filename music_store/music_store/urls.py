from django.urls import path

from . import views

app_name = 'music_store'

urlpatterns = [
    path('', views.home, name="home"),
    path('artist/', views.artist_listing, name="artists"),
    path('all-albums/', views.album_listing, name="all-albums"),
    path('albums/<int:artist_id>/', views.artist_album, name="author-albums"),
    path('artist/<int:artist_id>/', views.artist_detail, name="artist-detail"),
    path('album/<int:album_id>/', views.album_detail, name="album-detail"),
]