from django.contrib import admin
from .models import Listings, Photos, Scraper

# Register your models here.


class PhotoInLine(admin.TabularInline):
    model = Photos


class ListingsAdmin(admin.ModelAdmin):
    list_display = ('listing_id', 'listing_title',
                    'is_published', 'formatted_price', 'list_date', 'purchaseType', 'propertyType', 'realtor_id')

    list_display_links = ('listing_id', 'listing_title')
    list_filter = ('realtor_id',)
    list_editable = ('is_published',)
    search_fields = ('listing_title', 'city')
    list_per_page = 25

    inlines = [
        PhotoInLine,
    ]

    def formatted_price(self, obj):
        return '{0:,.0f} Rs'.format(obj.price)


# Register
admin.site.register(Listings, ListingsAdmin)


class ScraperAdmin(admin.ModelAdmin):
    list_display = ('scraper_id', 'scrapertitle',
                    'scraper_price')
    list_display_links = ('scraper_id', 'scrapertitle')
    list_per_page = 25

    def scraper_price(self, obj):
        return '{0:,.0f} Rs'.format(obj.price)


# Register
admin.site.register(Scraper, ScraperAdmin)
