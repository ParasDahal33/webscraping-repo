
import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Contact',
            fields=[
                ('id', models.AutoField(auto_created=True,
                 primary_key=True, serialize=False, verbose_name='ID')),
                ('listing_id', models.IntegerField(verbose_name='listing_id')),
                ('listing_title', models.CharField(
                    max_length=200, verbose_name='listing_title')),
                ('contact_name', models.CharField(
                    max_length=200, verbose_name='contact_name')),
                ('contact_mail', models.CharField(
                    max_length=200, verbose_name='contact_mail')),
                ('contact_phone', models.CharField(
                    max_length=200, verbose_name='contact_phone')),
                ('contact_message', models.TextField(
                    blank=True, verbose_name='contact_message')),
                ('contact_date', models.DateTimeField(
                    default=datetime.datetime.now)),
                ('user_id', models.IntegerField(blank=True)),
            ],
            options={
                'verbose_name': 'contact',
                'verbose_name_plural': 'contacts',
            },
        ),
    ]
