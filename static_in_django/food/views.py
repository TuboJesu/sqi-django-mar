from django.shortcuts import render

# Create your views here.

def menu(request):
    food_choice = ["Rice", "Beans", "Spaghetti", "Yam", "Noodles"]
    return render(request, "food/menu.html", {"food_choice": food_choice})

