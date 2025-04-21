# ~/projects/django-web-app/merchex/listings/views.py

from django.shortcuts import render, get_object_or_404

from listings.models import Band, Listing


def home(request):
    return render(request, "listings/home.html")


def bands(request):
    bands = Band.objects.all()
    return render(request, "listings/bands.html", context={"bands": bands})


def band_show(request, band_id):
    # band = Band.objects.get(id=band_id)
    band = get_object_or_404(Band, pk=band_id)
    return render(request, "listings/band_show.html", {"band": band})


def listings(request):
    """
    Return a simple HTML response with a title, a paragraph and a list of all the titles in the database.
    """

    listings = Listing.objects.all()
    return render(request, "listings/listings.html", context={"listings": listings})


def listing_show(request, listing_id):
    listing = get_object_or_404(Listing, pk=listing_id)
    return render(request, "listings/listing_show.html", {"listing": listing})


def about(request, target="YOOO"):
    return render(request, "listings/about.html", {"target": target})


def contact(request):
    return render(request, "listings/contact.html")
