from django.shortcuts import render, HttpResponse


# Create your views here.


def home(request):
    return HttpResponse("This is an index in http...")