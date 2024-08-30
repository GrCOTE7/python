# ~/projects/django-web-app/merchex/listings/views.py

from django.http import HttpResponse
from django.shortcuts import render

from listings.models import Band, Listing


def hello(request):
    """
    Return a simple HTML response with a title, a paragraph and a list of all the Bands in the database.
    """

    bands = Band.objects.all()
    return HttpResponse(
        f"""
        <h1>Hello Django</h1>
        <p>Groupes préférés :</p>
            <ul>
                <li>{ bands[0].name }</li>
                <li>{ bands[1].name }</li>
                <li>{ bands[2].name }</li>
            </ul>
        """
    )


def listings(request):
    """
    Return a simple HTML response with a title, a paragraph and a list of all the titles in the database.
    """

    listings = Listing.objects.all()
    return HttpResponse(
        f"""
        <h1>Listings</h1>
        <p>Titres :</p>
            <ul>
                <li>{ listings[0].title }</li>
                <li>{ listings[1].title }</li>
                <li>{ listings[2].title }</li>
                <li>{ listings[3].title }</li>
            </ul>
        """
    )


def about(request, target="YOOO"):
    """
    Return a simple HTML response with a title and a paragraph.
    The target parameter is used to display a variable value in the rendered HTML.
    """
    return HttpResponse(f"<h1>About US</h1><p>Paragraphe</p><p>Target = {target}</p>")


def contact(request):
    return HttpResponse("<h1>Contact US</h1><p>Paragraphe</p>")
