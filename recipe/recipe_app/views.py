from django.shortcuts import render, redirect

from .models import Recipe
from .forms import RecipeForm


# Create your views here.

def home(request):
    return render(request, "recipe/home.html", {"home": home})


def add_recipe(request):

    form = RecipeForm()

    if request.method == "POST":
        form = RecipeForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return redirect("recipe_app:recipes")
    
    context = {
        "form":form
    }

    return render(request, "recipe/add_recipe_with_form.html", context)


def all_recipe(request):
    all_recipe = Recipe.objects.all()
    return render(request, "recipe/all_recipe.html", {"recipes":all_recipe})


