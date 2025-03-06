from django.shortcuts import render, HttpResponse

def menu(request):
    return HttpResponse("These are the menus available...")

def contact(request):
    return HttpResponse("Contact us on FK-hotline")

# Create your views here.
