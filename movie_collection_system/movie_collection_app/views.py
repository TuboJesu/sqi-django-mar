from django.shortcuts import render, get_object_or_404, redirect

from django.urls import reverse

from .models import Movie
from .forms import CreateMovie, UpdateMovie, MovieSearchForm, FilterByGenre

from django.contrib.auth.decorators import login_required
from django.contrib import messages



def all_movies(request):
    all_movies = Movie.objects.all()
    form = MovieSearchForm(request.GET)

    if form.is_valid():
        title = form.cleaned_data.get('title')
        if title:
            all_movies = all_movies.filter(title__icontains = title)
    

    filter_form = FilterByGenre(request.GET)
    
    if filter_form.is_valid():
        genre = filter_form.cleaned_data.get('genre')
        if genre:
            all_movies = all_movies.filter(genre=genre)

    return render(request, 'movies/all_movies.html', {'movies':all_movies, "filter_form":filter_form})

@login_required
def create_movie(request):
    form = CreateMovie()

    if request.method == 'POST':
        form = CreateMovie(request.POST, request.FILES)
        if form.is_valid():

            new_movie = form.save(commit=False)
            new_movie.added_by = request.user
            new_movie.save()
            messages.success(request, 'Movie Created Successfully')
            return redirect('movie_collection_app:all_movies')
    
    context = {

        "form": form
    }
    return render(request, 'movies/create_movie.html', context)

@login_required
def movie_detail(request, movie_id):
    movie = get_object_or_404(Movie, pk=movie_id)

    return render(request, 'movies/movie_detail.html', {'movie':movie})

@login_required
def update_movie(request, movie_pk):
    movie = get_object_or_404(Movie, pk=movie_pk)
    if request.user != movie.added_by:
        messages.error(request, 'You do not have permission to update the Movie')
        return redirect('movie_collection_app:all_movies')
    
    update_movie = UpdateMovie(instance=movie)

    if request.method == 'POST':
        update_movie = UpdateMovie(request.POST, request.FILES, instance=movie)
        if update_movie.is_valid():
            update_movie.save()
            messages.success(request, 'You have Sucessfully updated a Movie')
            return redirect(reverse('movie_collection_app:movie_detail',kwargs={'movie_id': movie.id}))
    
    context = {

        "movie": movie,
        "form": update_movie
    }

    return render(request, 'movies/update_movies.html', context)

@login_required
def confirm_delete(request, movie_id):
    movie = get_object_or_404(Movie, pk=movie_id)
    if request.user != movie.added_by:
        messages.error(request, 'You do not have permission to delete the Movie')
        return redirect('movie_collection_app:all_movies')

    
    return render(request, 'movies/confirm_delete.html', {'movie':movie})

@login_required
def delete_movie(request, movie_id):
    movie = get_object_or_404(Movie, pk=movie_id)

    if request.user != movie.added_by:
        messages.error(request, 'You do not have permission to delete the Movie')
        return redirect('movie_collection_app:all_movies')

    if request.method == 'POST':
        movie.delete()
        messages.success(request, 'You have Suceesfully deleted a Movie')
        return redirect('movie_collection_app:all_movies')