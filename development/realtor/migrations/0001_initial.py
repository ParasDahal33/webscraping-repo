
import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Realtors',
            fields=[
                ('realtor_id', models.BigAutoField(
                    primary_key=True, serialize=False)),
                ('first_name', models.CharField(
                    max_length=200, verbose_name='First Name')),
                ('last_name', models.CharField(
                    max_length=200, verbose_name='Last Name')),
                ('photo', models.ImageField(
                    upload_to='realtor/%Y/%m/%d/', verbose_name='Realtor Photo')),
                ('description', models.TextField(
                    blank=True, verbose_name='Description')),
                ('phone', models.CharField(max_length=50, verbose_name='Phone Number')),
                ('email', models.EmailField(max_length=254, verbose_name='EMAIL')),
                ('is_mvp', models.BooleanField(default=False, verbose_name='MVP')),
                ('hire_date', models.DateTimeField(
                    blank=True, default=datetime.datetime.now)),
                ('created_at', models.DateTimeField(
                    editable=False, verbose_name='Created At')),
                ('updated_at', models.DateTimeField(
                    editable=False, verbose_name='Updated At')),
            ],
            options={
                'verbose_name': 'Realtor',
                'verbose_name_plural': 'Realtors',
            },
        ),
    ]
