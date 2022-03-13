import csv
import io
from cgitb import text
from multiprocessing import context
from django.shortcuts import render, redirect, get_object_or_404
from django.core.paginator import EmptyPage, PageNotAnInteger, Paginator
from .models import Listings, Photos, Scraper
from .choices import bedroom_choices, price_choices, state_choices, purchase_choices, property_choices
from contact.forms import InquiryModelForm
from django.contrib import messages
from django.contrib.auth.decorators import permission_required
# Create your views here.


def index(request):
    title = 'Real Estate Hunt Nepal | Listing'
    template = 'listing/index.html'

    # Order & Filter the context for the listing page.
    listings = Listings.objects.all().order_by(
        '-list_date').filter(is_published=True)

    paginator = Paginator(listings, 6)
    page = request.GET.get('page')
    paged_listings = paginator.get_page(page)

    context = {'title': title,
               'listings': paged_listings,
               }
    return render(request, template, context)


def detail(request, listing_id):
    title = 'Listing | Details'
    template_name = 'listing/detail.html'
    details = get_object_or_404(Listings, pk=listing_id)
    photos = Photos.objects.all().filter(listing_id=listing_id)
    if request.user.is_active:
        inquiry_form = InquiryModelForm(initial={
            'listing_id': listing_id,
            'listing_title': getattr(details, 'listing_title'),
            'contact_name': request.user.first_name + ' ' + request.user.last_name,
            'contact_mail': request.user.email,
            'user_id': request.user.id,
        })

    if request.user.is_anonymous:
        inquiry_form = InquiryModelForm(initial={
            'listing_id': listing_id,
            'listing_title': getattr(details, 'listing_title'),
        })

    context = {
        'title': title,
        'details': details,
        'photos': photos,
        'inquiry_form': inquiry_form,
    }
    return render(request, template_name, context)


def search(request):
    title = 'Search Result'
    template = 'listing/search.html'

    queryset_list = Listings.objects.order_by('-list_date')
    # Keywords
    if 'keywords' in request.GET:
        keywords = request.GET['keywords']
        if keywords:
            queryset_list = queryset_list.filter(
                description__icontains=keywords)
    # City
    if 'city' in request.GET:
        city = request.GET['city']
        if city:
            queryset_list = queryset_list.filter(
                city__iexact=city)
    # State
    if 'state' in request.GET:
        state = request.GET['state']
        if state:
            queryset_list = queryset_list.filter(
                state__iexact=state)
    # PurchaseType
    if 'purchaseType' in request.GET:
        purchaseType = request.GET['purchaseType']
        if purchaseType:
            queryset_list = queryset_list.filter(
                purchaseType__iexact=purchaseType)

     # PropertyType
    if 'propertyType' in request.GET:
        propertyType = request.GET['propertyType']
        if propertyType:
            queryset_list = queryset_list.filter(
                propertyType__iexact=propertyType)
    # Price
    if 'price' in request.GET:
        price = request.GET['price']
        if price:
            queryset_list = queryset_list.filter(
                price__lte=price)
    context = {'title': title,
               'listings': queryset_list,
               'state_choices': state_choices,
               'purchase_choices': purchase_choices,
               'property_choices': property_choices,
               'price_choices': price_choices,
               }
    return render(request, template, context)


def scraperDetail(request, scraper_id):
    title = 'Scraper | Details'
    template_name = 'listing/scraperDetails.html'
    scraperDetail = get_object_or_404(Scraper, pk=scraper_id)

    context = {
        'title': title,
        'details': scraperDetail,
    }
    return render(request, template_name, context)


def get_html_content(property):
    import requests
    USER_AGENT = "Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/44.0.2403.157 Safari/537.36"
    LANGUAGE = "en-US,en;q=0.5"
    session = requests.Session()
    session.headers['User-Agent'] = USER_AGENT
    session.headers['Accept-Language'] = LANGUAGE
    session.headers['Content-Language'] = LANGUAGE
    property = property.replace('', '+')
    html_content = session.get(
        f'https://www.realestateinnepal.com/search/?location={property}').content
    return html_content


def advanceSearch(request):
    title = 'Advance Search'
    template_name = 'listing/advanceSearch.html'
    scraper = Scraper.objects.all().order_by('scrapertitle')
    if 'keywords' in request.GET:
        keywords = request.GET['keywords']
        if keywords:
            scraper = scraper.filter(
                scrapertitle__icontains=keywords)
    # City
    if 'location' in request.GET:
        location = request.GET['location']
        if location:
            scraper = scraper.filter(
                scraper_location__iexact=location)
    # Price
    if 'price' in request.GET:
        price = request.GET['price']
        if price:
            scraper = scraper.filter(
                scraper_price__lte=price)

    context = {
        'title': title,
        'scraper': scraper,
        'price_choices': price_choices
    }
    return render(request, template_name, context)


@permission_required('admin.can_add_log_entry')
def csv_upload(request):
    template = 'listing/uploadCsv.html'
    if request.method == "GET":
        return render(request, template)
    csv_file = request.FILES['file']
    if not csv_file.name.endswith('.csv'):
        messages.error(request, 'This is not a csv file')
    data_set = csv_file.read().decode('UTF-8')
    io_string = io.StringIO(data_set)
    next(io_string)
    for column in csv.reader(io_string, delimiter=','):
        _, created = Scraper.objects.update_or_create(
            scrapertitle=column[0],
            scraper_location=column[1],
            scraper_price=column[2],
            scraper_image=column[3]
        )
    context = {}
    return render(request, template, context)
