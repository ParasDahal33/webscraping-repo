# Generated by Django 3.1 on 2022-03-05 07:27

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('appartment_listing', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='scraper',
            name='id',
        ),
        migrations.AddField(
            model_name='scraper',
            name='scraper_id',
            field=models.AutoField(default=1, primary_key=True, serialize=False, verbose_name='ID'),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='scraper',
            name='scrapertitle',
            field=models.CharField(max_length=255, verbose_name='ScraperTitle'),
        ),
    ]
