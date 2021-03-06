
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('contact', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='contact',
            name='contact_mail',
            field=models.CharField(max_length=200, verbose_name='E-Mail'),
        ),
        migrations.AlterField(
            model_name='contact',
            name='contact_message',
            field=models.TextField(blank=True, verbose_name='Message'),
        ),
        migrations.AlterField(
            model_name='contact',
            name='contact_name',
            field=models.CharField(
                max_length=200, verbose_name='Contact Name'),
        ),
        migrations.AlterField(
            model_name='contact',
            name='contact_phone',
            field=models.CharField(max_length=200, verbose_name='Phone'),
        ),
        migrations.AlterField(
            model_name='contact',
            name='listing_id',
            field=models.IntegerField(verbose_name='Listing ID'),
        ),
        migrations.AlterField(
            model_name='contact',
            name='listing_title',
            field=models.CharField(max_length=200, verbose_name='Title'),
        ),
        migrations.AlterField(
            model_name='contact',
            name='user_id',
            field=models.IntegerField(blank=True, null=True),
        ),
    ]
