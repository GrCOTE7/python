from django.contrib import admin

from listings.models import Band, Listing


class BandAdmin(admin.ModelAdmin):

    list_display = ("name", "genre", "biography", "year_formed", "active")


class ListingAdmin(admin.ModelAdmin):

    list_display = ("title", "band", "description", "price", "types", "year")


admin.site.register(Band, BandAdmin)
admin.site.register(Listing, ListingAdmin)
