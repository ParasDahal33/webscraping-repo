from django.db import models
from datetime import datetime
from .choices import purchase_choices, property_choices
from realtor.models import Realtors

# Create your models here.


class Listings(models.Model):
    listing_id = models.AutoField(
        verbose_name='ID',
        primary_key=True,
    )
    realtor_id = models.ForeignKey(Realtors, on_delete=models.DO_NOTHING)
    listing_title = models.CharField(
        max_length=100,
        verbose_name='Title',
    )
    state = models.CharField(max_length=100, verbose_name='State')
    district = models.CharField(max_length=100, verbose_name='District')
    city = models.CharField(max_length=100, verbose_name='City')
    description = models.TextField(blank=True, verbose_name='Description')
    price = models.DecimalField(
        verbose_name='Price', max_digits=15, decimal_places=5)
    purchaseType = models.CharField(unique=True,
                                    default="Buy", max_length=8, verbose_name='PurchaseType')
    propertyType = models.CharField(unique=True,
                                    default="House", max_length=15, verbose_name='PropertyType')
    bedroom = models.IntegerField(
        verbose_name='Bedroom', default=None, blank=True, null=True)
    bathroom = models.IntegerField(
        verbose_name='Bathroom', default=None, blank=True, null=True)
    garage = models.IntegerField(
        verbose_name='Garage', default=None, blank=True, null=True)
    sqft = models.IntegerField(
        verbose_name='Sqft', default=None, blank=True, null=True)
    photo_main = models.ImageField(
        upload_to='photos/%Y/%m/%d/', verbose_name='Main Photo', default=None, blank=True, null=True)
    is_published = models.BooleanField(default=True, verbose_name='Published')
    list_date = models.DateTimeField(
        default=datetime.now, blank=True, verbose_name='List Date')

    class Meta():
        verbose_name = 'Listing'
        verbose_name_plural = 'Listings'

    def __str__(self):
        return self.listing_title


class Photos(models.Model):
    listing_id = models.ForeignKey(Listings, on_delete=models.CASCADE)
    photo = models.ImageField(upload_to='photos/%Y/%m/%d/', blank=True)

    class Meta():
        verbose_name = 'Photo'
        verbose_name_plural = 'Photos'


class Scraper(models.Model):
    scraper_id = models.AutoField(
        verbose_name='ID',
        primary_key=True,
    )
    scrapertitle = models.CharField(
        max_length=255,
        verbose_name='ScraperTitle',
    )
    scraper_location = models.CharField(
        max_length=100,
        verbose_name='ScraperLocation',
    )
    scraper_price = models.CharField(
        max_length=100,
        verbose_name='ScraperPrice',
    )

    class Meta():
        verbose_name = 'Scraper'
        verbose_name_plural = 'Scrapers'
