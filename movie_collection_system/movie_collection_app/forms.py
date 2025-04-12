from django import forms

from .models import Movie, GenreChoices

class CreateMovie(forms.ModelForm):
    class Meta:
        model = Movie
        fields = ['title', 'director', 'release_date', 'description', 'poster', 'genre']



class UpdateMovie(forms.ModelForm):
    class Meta:
        model = Movie
        fields = ['title', 'director', 'release_date', 'description', 'poster', 'genre']



class MovieSearchForm(forms.Form):
    title = forms.CharField(max_length=255, required=False)

class FilterByGenre(forms.Form):
    genre = forms.ChoiceField(choices=GenreChoices.choices, required=False)