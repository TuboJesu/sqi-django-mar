from django.shortcuts import render, get_object_or_404

# Create your views here.

from .models import Artist
from .models import Album


def home(request):

    return render(request, "music-store/home.html")


def artist_listing(request):

    get_all_artists = Artist.objects.order_by("debut_year")
    
    return render(request, "music-store/artist-listing.html", {"all_artists": get_all_artists})

def album_listing(request):

    get_all_albums = Album.objects.order_by("-release_date")
    return render(request, "music-store/album-listing.html", {"all_albums": get_all_albums})


def artist_album(request, artist_id):
    artist = get_object_or_404(Artist, id=artist_id)  
    get_artist_albums = Album.objects.order_by("-release_date")  

    context = {
        "artist": artist,
        "artist_albums": get_artist_albums
    }
    
    return render(request, "music-store/artist-album.html", context)

def artist_detail(request, artist_id):
    artist = get_object_or_404(Artist, id=artist_id)  

    return render(request, "music-store/artist_detail.html", {"artist": artist})

def album_detail(request, album_id):
    album = get_object_or_404(Album, id=album_id)  

    return render(request, "music-store/album_detail.html", {"album": album})

