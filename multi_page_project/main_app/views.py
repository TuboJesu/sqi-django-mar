from django.shortcuts import render


def home(request):
    return render(request, "main_app/home.html")

def contact(request):
    return render(request, "main_app/contact.html")

def about(request):
    return render(request, "main_app/about.html")

