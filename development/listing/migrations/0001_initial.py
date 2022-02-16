
import datetime
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('realtor', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Listings',
            fields=[
                ('listing_id', models.AutoField(
                    primary_key=True, serialize=False, verbose_name='ID')),
                ('listing_title', models.CharField(
                    max_length=100, verbose_name='Title')),
                ('street', models.CharField(max_length=100,
                 verbose_name='Street')),
                ('city', models.CharField(max_length=100,
                 verbose_name='City')),
                ('state', models.CharField(max_length=100,
                 verbose_name='State')),
                ('zipcode', models.CharField(max_length=100,
                 verbose_name='ZipCode')),
                ('description', models.TextField(
                    blank=True, verbose_name='Description',  null=True)),
                ('price', models.DecimalField(decimal_places=5,
                 max_digits=15, verbose_name='Price')),
                ('bedroom', models.IntegerField(
                    verbose_name='Bedroom',  blank=True,  null=True)),
                ('bathroom', models.DecimalField(
                    decimal_places=1, max_digits=2, verbose_name='Bathroom')),
                ('garage', models.IntegerField(
                    default=0, verbose_name='Garage')),
                ('sqft', models.IntegerField(
                    verbose_name='Sqft')),
                ('lot_size', models.DecimalField(
                    decimal_places=1, max_digits=5, verbose_name='Lot Size')),
                ('photo_main', models.ImageField(
                    upload_to='photos/%Y/%m/%d/', verbose_name='Main Photo')),
                ('is_published', models.BooleanField(
                    default=True, verbose_name='Published')),
                ('list_date', models.DateTimeField(
                 default=datetime.datetime.now, verbose_name='List Date')),
                ('realtor_id', models.ForeignKey(
                    on_delete=django.db.models.deletion.DO_NOTHING, to='realtor.Realtors')),
            ],
            options={
                'verbose_name': 'Listing',
                'verbose_name_plural': 'Listings',
            },
        ),
        migrations.CreateModel(
            name='Photos',
            fields=[
                ('id', models.AutoField(auto_created=True,
                 primary_key=True, serialize=False, verbose_name='ID')),
                ('photo', models.ImageField(blank=True, upload_to='photos/%Y/%m/%d/')),
                ('listing_id', models.ForeignKey(
                    on_delete=django.db.models.deletion.CASCADE, to='listing.Listings')),
            ],
            options={
                'verbose_name': 'Photo',
                'verbose_name_plural': 'Photos',
            },
        ),
    ]
