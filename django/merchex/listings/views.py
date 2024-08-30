# ~/projects/django-web-app/merchex/listings/views.py

from django.shortcuts import render, HttpResponse

from listings.models import Band, Listing


def hello(request):
    bands = Band.objects.all()
    return render(request, "listings/hello.html", context={"bands": bands})


def listings(request):
    """
    Return a simple HTML response with a title, a paragraph and a list of all the titles in the database.
    """

    listings = Listing.objects.all()
    return render(request, 'listings/listings.html', context={"listings": listings})


def about(request, target="YOOO"):
    return render(request, 'listings/about.html', {'target': target})


def contact(request):
    return HttpResponse("<h1>Contact US</h1><p>Paragraphe</p>")
