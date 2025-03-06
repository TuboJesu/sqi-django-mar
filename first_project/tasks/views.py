from django.shortcuts import render, HttpResponse


def homepage(request):
    return HttpResponse("This is the hompage...")

def all_tasks(request):
    return HttpResponse("These are all the tasks")

# Create your views here.
