from django.shortcuts import render

from django.utils import timezone

# Create your views here.

def homepage(request):
    return render(request, "my_bakery/homepage.html")

def aboutpage(request):

    return render(request, "my_bakery/aboutpage.html", {"bakery_name": "JESU BAKERY"})

def contactpage(request):

    current_time = timezone.localtime().time()
    opening_time = timezone.datetime.strptime("02:00", "%H:%M").time()
    closing_time = timezone.datetime.strptime("14:00", "%H:%M").time()

    is_open = opening_time <= current_time <= closing_time

    return render(request, "my_bakery/contactpage.html", {"is_open": is_open})

def menupage(request):

    bakery_menu = {
    "Croissant": 2.99,
    "Baguette": 3.49,
    "Chocolate Cake": 4.99,
    "Cupcake": 2.99,
    "Coffee": 2.49,
    "Tea": 1.99
}
    return render(request, "my_bakery/menupage.html", {"bakery_menu": bakery_menu})



