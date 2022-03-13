from django.urls import path
from . import views

app_name = 'listing'

urlpatterns = [
    path('', views.index, name='index'),
    path('<int:listing_id>', views.detail, name='detail'),
    path('<int:scraper_id>', views.scraperDetail, name='scraperDetail'),
    path('search', views.search, name='search'),
    path('advanceSearch', views.advanceSearch, name='advanceSearch'),
    path('upload-csv', views.csv_upload, name="csv_upload")
]
