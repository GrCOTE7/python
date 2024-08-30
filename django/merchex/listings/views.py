# ~/projects/django-web-app/merchex/listings/views.py

from django.http import HttpResponse
from django.shortcuts import render


def hello(request):
    return HttpResponse("<h1>Hello Django!</h1><p>Paragraphe</p>")

def listings(request):
    return HttpResponse("<h1>Listings</h1><p>Paragraphe</p>")


def about(request, target="YOOO"):
    return HttpResponse(f"<h1>About US</h1><p>Paragraphe</p><p>Target = {target}</p>")


def contact(request):
    return HttpResponse("<h1>Contact US</h1><p>Paragraphe</p>")
